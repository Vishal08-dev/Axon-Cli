import ollama

from axon import config


def stream_response(conversation_history):
    """Streams response tokens from Ollama one by one."""
    bot = ollama.chat(
        model=config.current_model, messages=conversation_history, stream=True
    )
    for chunk in bot:
        yield chunk["message"]["content"]
