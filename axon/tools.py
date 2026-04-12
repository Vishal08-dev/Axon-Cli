import os
import subprocess


def load_project(folder_path):
    allowed = [
        ".py",
        ".js",
        ".html",
        ".css",
        ".json",
        ".md",
        ".txt",
        ".ts",
        ".jsx",
        ".tsx",
    ]
    skip_folders = ["node_modules", ".git", "__pycache__", ".venv", "venv"]
    result = ""
    file_count = 0
    for root, dirs, files in os.walk(folder_path):
        # skip junk folders
        dirs[:] = [d for d in dirs if d not in skip_folders]
        for file in files:
            _, ext = os.path.splitext(file)
            if ext not in allowed:
                continue
            full_path = os.path.join(root, file)
            content = read_file(full_path)
            result += f"\n=== {full_path} ===\n{content}\n"
            file_count += 1
    if file_count == 0:
        return "No supported files found in that folder."
    return f"Loaded {file_count} files:\n{result}"


def parse_tool_call(text):
    if "<tool>" not in text:
        return (None, None)

    start = text.find("<tool>") + len("<tool>")
    end = text.find("</tool>")
    tool_name = text[start:end]

    start = text.find("<args>") + len("<args>")
    end = text.find("</args>")
    args = text[start:end]

    return (tool_name, args)


def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: file '{file_path}' not found."


def write_file(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
        return f"Success: file '{file_path}' written."
    except Exception as e:
        return f"Error: {e}"


def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        # if there is output return it, otherwise return errors
        if result.stdout:
            return result.stdout
        elif result.stderr:
            return result.stderr
        else:
            return "Command ran successfully with no output."
    except Exception as e:
        return f"Error: {e}"
