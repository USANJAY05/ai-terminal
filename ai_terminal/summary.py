import os
import typer
from rich.console import Console
from rich.markdown import Markdown

# ✅ FIX: Import from llm_config, not main
from .llm_config import llm, summary_prompt

console = Console()
app = typer.Typer()

@app.command()
def summary(file: str, save: bool = typer.Option(False, "--save", help="Save summary to a file")):
    """📄 Summarize a text file."""
    filepath = os.path.abspath(file)
    if not os.path.isfile(filepath):
        console.print(f"[bold red]❌ File not found:[/bold red] {filepath}")
        raise typer.Exit()

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if not content.strip():
            console.print("[yellow]⚠️ The file is empty.[/yellow]")
            raise typer.Exit()

        formatted_prompt = summary_prompt.format(content=content[:4000])
        summary_text = llm.invoke(formatted_prompt).content.strip()

        markdown_text = f"## 📌 Summary of `{os.path.basename(filepath)}`\n\n{summary_text}\n"

        console.print("\n[bold green]---[/bold green]\n")
        console.print(Markdown(markdown_text))
        console.print("\n[bold green]---[/bold green]\n")

        if save:
            summary_filename = f"{filepath}.summary"
            with open(summary_filename, "w", encoding="utf-8") as f:
                f.write(markdown_text)
            console.print(f"[bold cyan]💾 Summary saved to:[/bold cyan] {summary_filename}")

    except Exception as e:
        console.print(f"[bold red]❌ Error reading file:[/bold red] {e}")
