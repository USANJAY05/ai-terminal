from rich.console import Console
from rich.markdown import Markdown
from langchain.schema import HumanMessage, AIMessage
from .llm_config import llm
from .utils import save_chat_history

console = Console()

def chat(save: bool = False):
    """🤖 Chatbot Mode with memory."""
    console.print("[bold cyan]🤖 Entering Chatbot Mode. Type 'exit' or 'quit' to return.[/bold cyan]\n")
    chat_history = []

    while True:
        user_input = input("Chatbot> ")

        if user_input.lower() in ["exit", "quit"]:
            if save:
                save_chat_history([f"User: {m.content}" if isinstance(m, HumanMessage)
                                   else f"Assistant: {m.content}" for m in chat_history])
            console.print("[bold cyan]👋 Exiting Chatbot Mode.[/bold cyan]")
            break

        chat_history.append(HumanMessage(content=user_input))
        try:
            response = llm.invoke(chat_history).content.strip()
            chat_history.append(AIMessage(content=response))
            console.print("\n[bold green]---[/bold green]\n")
            console.print(Markdown(response))
            console.print("\n[bold green]---[/bold green]\n")
        except Exception as e:
            console.print(f"[bold red]❌ Chatbot Error:[/bold red] {e}")
