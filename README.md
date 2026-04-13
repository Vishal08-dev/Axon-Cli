# AXON 🤖
> A local CLI AI assistant powered by Ollama — works like Gemini CLI or Claude Code, completely offline and private.

## Features
- 🧠 Conversational AI with full memory across turns
- 🌊 Streaming responses with a thinking spinner
- 📄 Markdown rendering in the terminal
- 📁 Read, write files in your current directory
- ⚡ Run shell commands directly from chat
- 📂 Load full project folders into context
- 💾 Save and load chat sessions
- 🔀 Switch between Ollama models at runtime
- ⌨️ Slash command autocomplete

## Requirements
- Python 3.10+
- [Ollama](https://ollama.com) installed and running
- At least one Ollama model pulled (e.g. `ollama pull llama3.2`)

## Installation

**Option 1 — Install via pip (recommended)**

    pip install axon-cli
    axon

**Option 2 — Clone and install locally**

    git clone https://github.com/Vishal08-dev/Axon-Cli.git
    cd Axon-Cli
    pip install -e .
    axon

**Make sure Ollama is running**

    ollama serve

## Usage

On startup, AXON will ask you to select a model from your installed Ollama models using arrow keys. Then you can start chatting right away.

    ? Select a model to start with:
     ❯ llama3.2:latest
       gemma4:E4B

## Commands

| Command | Description |
|---|---|
| `/help` | Show all available commands |
| `/clear` | Clear conversation history |
| `/save` | Save current session to disk |
| `/load` | Load a previously saved session |
| `/model` | Switch Ollama model at runtime |
| `/load-project` | Load a full project folder into context |
| `/exit` | Quit AXON |

## Tools

AXON can interact with your filesystem and shell when asked:

- **Read a file** — `read the file main.py`
- **Write a file** — `write a file called notes.txt with...`
- **Run a command** — `run dir` or `run git status`
- **Load a project** — `/load-project` then provide folder path

## Project Structure

    axon-cli/
    ├── axon/
    │   ├── __init__.py
    │   ├── main.py        # Entry point and main loop
    │   ├── llm.py         # Ollama streaming client
    │   ├── memory.py      # Conversation history management
    │   ├── renderer.py    # Rich terminal UI and markdown rendering
    │   ├── commands.py    # Slash command handler
    │   ├── tools.py       # File and shell tools
    │   └── config.py      # Shared configuration
    ├── sessions/          # Saved chat sessions (auto-created)
    ├── pyproject.toml
    ├── requirements.txt
    └── README.md

## Built With

- [Ollama](https://ollama.com) — local LLM inference
- [Rich](https://github.com/Textualize/rich) — terminal UI and markdown
- [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit) — autocomplete input
- [pyfiglet](https://github.com/pwaller/pyfiglet) — ASCII art banner
- [questionary](https://github.com/tmbo/questionary) — interactive model selection

## License
MIT
