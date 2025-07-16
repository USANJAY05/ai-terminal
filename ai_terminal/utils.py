import os
import subprocess
from rich.console import Console

console = Console()

def is_command_safe(command: str) -> bool:
    blocked_keywords = [
        "rm -rf", "mkfs", "shutdown", "reboot", "dd", "wget", "curl",
        ":(){", ">:(", "mv /", "chmod 777 /", "chown root"
    ]
    return not any(word in command for word in blocked_keywords)

def run_command(command: str, cwd: str):
    if not command.strip():
        console.print("⚠️ No valid command generated.")
        return cwd

    if not is_command_safe(command):
        console.print(f"❌ Command blocked for safety: {command}")
        return cwd

    if command.startswith("cd"):
        parts = command.split(maxsplit=1)
        new_path = os.path.expanduser("~") if len(parts) == 1 else os.path.abspath(os.path.join(cwd, parts[1]))
        if os.path.isdir(new_path):
            console.print(f"📂 Changed directory to: {new_path}")
            return new_path
        else:
            console.print(f"❌ Directory not found: {new_path}")
            return cwd

    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True, cwd=cwd)
        console.print(f"[bold green]Output:[/bold green]\n{result.stdout}")
        if result.stderr:
            console.print(f"[bold red]Error:[/bold red]\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        console.print(f"❌ Error executing command: {e}")

    return cwd

def save_chat_history(chat_history, filename="chat_history.md"):
    if not chat_history:
        console.print("[yellow]⚠️ No chat history to save.[/yellow]")
        return

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("# 🤖 Chat History\n\n")
            for entry in chat_history:
                role, message = entry.split(":", 1)
                f.write(f"**{role.strip()}**: {message.strip()}\n\n")
        console.print(f"[bold cyan]💾 Chat history saved to:[/bold cyan] {filename}")
    except Exception as e:
        console.print(f"[bold red]❌ Error saving chat history:[/bold red] {e}")
