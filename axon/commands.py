import ollama
import questionary
from rich.console import Console

from axon import config, memory, tools

console = Console()


def handle_command(user_input):
    if user_input == "/help":
        print("/help - show commands")
        print("/clear - clear history")
        print("/save - save current session")
        print("/load - load a saved session")
        print("/model - change model")
        print("/load-project - load a project folder into context")
        print("/exit - quit")
        return True
    elif user_input == "/clear":
        memory.clear_history()
        return True
    elif user_input == "/exit":
        exit()
        return True
    elif user_input == "/save":
        filename = input("Enter session name: ")
        memory.save_session(filename)
        print(f"Session saved as '{filename}'")
        return True
    elif user_input == "/load":
        filename = input("Enter session name to load: ")
        memory.load_session(filename)
        print(f"Session '{filename}' loaded!")
        return True
    elif user_input == "/model":
        models = ollama.list()
        model_names = model_names = [
            m.model for m in models.models if m.model is not None
        ]
        selected = questionary.select("Select a model:", choices=model_names).ask()
        if selected:
            config.current_model = selected
            print(f"Model switched to '{selected}'")
        return True
    elif user_input == "/load-project":
        folder = input("Enter folder path: ")
        print("Loading project...")
        result = tools.load_project(folder)
        memory.add_message("user", f"Here is my project:\n{result}")
        console.print("[green]Project loaded![/green]")
        return True
    else:
        return False
