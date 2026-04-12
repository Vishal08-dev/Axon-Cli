import ollama
import questionary
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import WordCompleter

from axon import commands, config, memory, tools
from axon.llm import stream_response
from axon.renderer import print_welcome, render_markdown, thinking

models = ollama.list()
model_names = [m.model for m in models.models if m.model is not None]
selected = questionary.select(
    "Select a model to start with:", choices=model_names
).ask()
config.current_model = selected
print(f"Starting with '{selected}'\n")
print_welcome()

command_completer = WordCompleter(
    ["/help", "/clear", "/save", "/load", "/model", "/load-project", "/exit"],
    sentence=True,
)

session = PromptSession(completer=command_completer)


def main():
    while True:
        user_input = session.prompt("\n[>] ")
        if user_input.startswith("/"):
            commands.handle_command(user_input)
        else:
            memory.add_message("user", user_input)
            response = stream_response(memory.conversation_history)
            with thinking():
                full_response = ""
                for token in response:
                    full_response += token
            tool, args = tools.parse_tool_call(full_response)
            if tool == "read_file":
                args = args.split("/")[-1].strip()
                result = tools.read_file(args)
                memory.add_message("assistant", full_response)
                memory.add_message("user", f"Tool result:\n{result}")
                with thinking():
                    full_response = ""
                    response = stream_response(memory.conversation_history)
                    for token in response:
                        full_response += token
            elif tool == "run_command":
                result = tools.run_command(args)
                memory.add_message("assistant", full_response)
                memory.add_message("user", f"Tool result:\n{result}")
                with thinking():
                    full_response = ""
                    response = stream_response(memory.conversation_history)
                    for token in response:
                        full_response += token
            elif tool == "write_file":
                filepath, content = args.split("|", 1)
                filepath = filepath.split("/")[-1].strip()
                result = tools.write_file(filepath, content)
                memory.add_message("assistant", full_response)
                memory.add_message("user", f"Tool result:\n{result}")
                with thinking():
                    full_response = ""
                    response = stream_response(memory.conversation_history)
                    for token in response:
                        full_response += token
            render_markdown(full_response)
            memory.add_message("assistant", full_response)


if __name__ == "__main__":
    main()
