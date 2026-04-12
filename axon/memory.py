import json

conversation_history = [
    {
        "role": "system",
        "content": """You are AXON, a helpful CLI assistant running locally via Ollama.

        ONLY use tools when the user EXPLICITLY asks you to read, write, or run something.
        NEVER use tools to answer general questions — just respond normally.

        To read a file respond ONLY with:
        <tool>read_file</tool><args>filepath</args>

        To run a command respond ONLY with:
        <tool>run_command</tool><args>command</args>

        To write a file respond ONLY with:
        <tool>write_file</tool><args>filepath|content</args>

        Use the EXACT filename the user mentioned. Never use placeholder paths.
        For everything else including explaining code, answering questions, summarizing — respond normally and be concise.""",
    }
]


def add_message(role, content):
    conversation_history.append({"role": role, "content": content})


def clear_history():
    conversation_history[:] = [conversation_history[0]]


def save_session(filename):
    with open(f"sessions/{filename}.json", "w") as f:
        json.dump(conversation_history, f, indent=2)


def load_session(filename):
    with open(f"sessions/{filename}.json", "r") as f:
        data = json.load(f)
        conversation_history[:] = data
