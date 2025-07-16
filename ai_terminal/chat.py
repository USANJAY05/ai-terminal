from rich.console import Console
from rich.markdown import Markdown
from langchain.schema import HumanMessage, AIMessage
from .llm_config import llm
from .utils import save_chat_history

console = Console()

def chat():
    """ Chatbot Mode with memory."""
    console.print("[bold cyan] Entering Chatbot Mode. Type 'exit', 'quit', or 'exit --save [filename]' to return.[/bold cyan]\n")
    chat_history = []

    while True:
        user_input = input("Chatbot> ").strip()

        #  Handle exit / quit / exit --save
        if user_input.lower().startswith("exit") or user_input.lower().startswith("quit"):
            parts = user_input.split()

            if len(parts) >= 2 and parts[1] == "--save":
                filename = parts[2] if len(parts) == 3 else "chat_history.txt"
                try:
                    save_chat_history(
                        [f"User: {m.content}" if isinstance(m, HumanMessage)
                         else f"Assistant: {m.content}" for m in chat_history],
                        filename=filename  #  Modified to support custom filename
                    )
                    console.print(f"[bold green] Chat history saved to '{filename}'[/bold green]")
                except Exception as e:
                    console.print(f"[bold red] Error saving chat history:[/bold red] {e}")

            console.print("[bold cyan] Exiting Chatbot Mode.[/bold cyan]")
            break

        # Normal Chat Flow
        chat_history.append(HumanMessage(content=user_input))
        try:
            response = llm.invoke(chat_history).content.strip()
            chat_history.append(AIMessage(content=response))
            console.print("\n[bold green]---[/bold green]\n")
            console.print(Markdown(response))
            console.print("\n[bold green]---[/bold green]\n")
        except Exception as e:
            console.print(f"[bold red] Chatbot Error:[/bold red] {e}")
