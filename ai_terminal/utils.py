import os
from datetime import datetime
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
        console.print(" No valid command generated.")
        return cwd

    if not is_command_safe(command):
        console.print(f" Command blocked for safety: {command}")
        return cwd

    if command.startswith("cd"):
        parts = command.split(maxsplit=1)
        new_path = os.path.expanduser("~") if len(parts) == 1 else os.path.abspath(os.path.join(cwd, parts[1]))
        if os.path.isdir(new_path):
            console.print(f"📂 Changed directory to: {new_path}")
            return new_path
        else:
            console.print(f" Directory not found: {new_path}")
            return cwd

    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True, cwd=cwd)
        console.print(f"[bold green]Output:[/bold green]\n{result.stdout}")
        if result.stderr:
            console.print(f"[bold red]Error:[/bold red]\n{result.stderr}")
    except subprocess.CalledProcessError as e:
        console.print(f" Error executing command: {e}")

    return cwd

def save_chat_history(messages, filename="chat_history.txt"):
    """Save chat history to a file."""
    
    # Optional: Automatically create a 'chats' folder
    os.makedirs("chats", exist_ok=True)

    #  If default filename, add timestamp to avoid overwriting
    if filename == "chat_history.txt":
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"chats/chat_{timestamp}.txt"
    else:
        filename = f"chats/{filename}" if not filename.startswith("chats/") else filename

    with open(filename, "a", encoding="utf-8") as f:
        f.write("\n".join(messages))
        f.write("\n" + "=" * 50 + "\n")  # separator for sessions