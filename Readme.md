
# AI Terminal (ai-terminal)

An **AI-powered Linux terminal assistant** that can:

 **Generate safe Linux commands** using AI
 **Summarize text files intelligently**
 **Act as a chatbot with memory**
 **Save chat history for later reference**

Built with **LangChain**, **Google Gemini**, and **Rich** for a clean CLI experience.

---

## Features

### **AI Terminal Mode (`ati`)**

* Ask natural language questions like:

  ```
  AI Terminal> list files in the current directory
  ```
* AI responds with **safe Linux commands** and executes them automatically.
* Automatically blocks dangerous commands (`rm -rf`, `mkfs`, etc.).

### **Chatbot Mode**

* Conversational AI with memory.
* Save your chat history with:

  ```
  exit --save my_chat.txt
  ```

### **Text Summarizer**

* Summarize long text files into 3-5 concise sentences.
* Save summaries with the `--save` flag.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-terminal.git
cd ai-terminal
```

### 2. Run the Installer

```bash
chmod +x install.sh
./install.sh
```

This will:
 Create a virtual environment
 Install dependencies in **editable mode**
 Set up the `ati` command

---

## Configuration

### 1. Set Google API Key

Create a `.env` file in the project root:

```
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

### 2. Activate Virtual Environment (if needed)

```bash
source .venv/bin/activate
```

---

##  Usage

### **Start AI Terminal Mode**

```bash
./run.sh
```

or (if installed globally):

```bash
ati
```

### **Run Chatbot Mode**

```bash
ati chat
```

### **Summarize a File**

```bash
ati summary myfile.txt
```

Save the summary:

```bash
ati summary myfile.txt --save
```

---

##  Project Structure

```
ai-terminal/
├── ai_terminal/
│   ├── main.py         # CLI entry point (typer app)
│   ├── chat.py         # Chatbot mode
│   ├── terminal.py     # AI Terminal mode
│   ├── summary.py      # Text summarizer
│   ├── utils.py        # Helper functions (safe command execution, chat history)
│   ├── llm_config.py   # Google Gemini LLM configuration
├── install.sh          # Installer script
├── run.sh              # Run the CLI easily
├── uninstall.sh        # Uninstall & remove venv
├── setup.py            # Python package configuration
└── README.md           # This file
```

---

## Safety Features

 Blocks destructive commands (`rm -rf`, `dd`, `mkfs`, etc.)
 Asks before saving files
 Creates a separate `chats/` folder for history

---

## 🗑️ Uninstallation

```bash
chmod +x uninstall.sh
./uninstall.sh
```

This removes the virtual environment and uninstalls the package.
