import os

import pyfiglet
from rich.columns import Columns
from rich.console import Console
from rich.live import Live
from rich.markdown import Markdown
from rich.panel import Panel
from rich.spinner import Spinner
from rich.text import Text

from axon import config

console = Console()


def print_token(token):
    print(token, end="", flush=True)


def render_markdown(markdown_text):
    md = Markdown(markdown_text)
    console.print(md)


def thinking():
    return Live(Spinner("dots", text=" Thinking..."), console=console)


def print_banner():
    ascii_art = pyfiglet.figlet_format("AXON", font="slant")
    text = Text(ascii_art)
    text.stylize("bold cyan")
    console.print(text)


def print_welcome():
    print_banner()

    left_content = Text()
    left_content.append("\n  Welcome back!\n\n", style="bold white")
    left_content.append("  ◈\n\n", style="bold cyan")
    left_content.append(f"  {config.current_model}\n", style="dim")
    left_content.append("  Local via Ollama\n", style="dim")
    left_panel = Panel(left_content, style="cyan", width=35)

    sessions = os.listdir("sessions") if os.path.exists("sessions") else []
    activity = (
        f"Last session: {sorted(sessions)[-1].replace('.json', '')}"
        if sessions
        else "No recent activity"
    )

    right_content = Text()
    right_content.append("Tips for getting started\n\n", style="bold yellow")
    right_content.append("1. Ask questions, edit files, or run commands.\n")
    right_content.append("2. Use /load-project to load a full codebase.\n")
    right_content.append("3. Use /model to switch models.\n\n")
    right_content.append("Recent activity\n\n", style="bold yellow")
    right_content.append(activity, style="dim")
    right_panel = Panel(right_content, style="cyan", width=60)

    console.print(Columns([left_panel, right_panel]))
    console.print()
