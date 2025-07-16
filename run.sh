#!/bin/bash

echo "Running ai-terminal..."

# 1. Check if venv exists
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found! Run ./install.sh first."
    exit 1
fi

# 2. Activate venv
source .venv/bin/activate

# 3. Run the CLI
echo "Environment ready. Starting ai-terminal..."
ati "$@"
