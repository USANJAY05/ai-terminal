import os
import typer
from rich.console import Console
from .llm_config import llm, command_prompt
from .utils import run_command

console = Console()
app = typer.Typer()

@app.command()
def terminal():
    """💻 AI-powered Linux command generator."""
    current_dir = os.getcwd()
    console.print("[bold cyan]💻 AI Terminal Mode. Type 'exit' to quit.[/bold cyan]\n")

    while True:
        inp = input(f"AI Terminal ({current_dir})> ")

        if inp.lower() in ["exit", "quit"]:
            console.print("[bold cyan]👋 Exiting AI Terminal Mode.[/bold cyan]")
            break

        formatted_prompt = command_prompt.format(question=inp)
        try:
            generated_response = llm.invoke(formatted_prompt).content.strip()
            commands = [cmd.strip() for cmd in generated_response.split("\n") if cmd.strip()]
            for cmd in commands:
                current_dir = run_command(cmd, current_dir)
        except Exception as e:
            console.print(f"[bold red]❌ LLM Error:[/bold red] {e}")
