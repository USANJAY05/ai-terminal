#!/bin/bash

echo "🚀 Setting up ai-terminal environment..."

# 1. Create virtual environment if not exists
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment (.venv)..."
    python3 -m venv .venv
else
    echo "✅ Virtual environment already exists."
fi

# 2. Activate virtual environment
echo "✅ Activating virtual environment..."
source .venv/bin/activate

# 3. Upgrade pip
echo "⬆️  Upgrading pip..."
pip install --upgrade pip

# 4. Install in editable mode
echo "📦 Installing ai-terminal in editable mode..."
pip install -e .

echo "✅ Installation complete!"
echo ""
echo "👉 To start using, run:"
echo "   ./run.sh"
