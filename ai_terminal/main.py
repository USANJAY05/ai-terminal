import typer
from .chat import chat
from .summary import summary
from .terminal import terminal

app = typer.Typer()

# Register commands
app.command()(chat)
app.command()(summary)
app.command()(terminal)

# Run terminal by default when no command is given
@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        terminal()

if __name__ == "__main__":
    app()
