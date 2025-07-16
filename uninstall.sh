#!/bin/bash

echo "🗑️ Uninstalling ait..."

if [ -d ".venv" ]; then
    echo "✅ Activating virtual environment..."
    source .venv/bin/activate

    echo "📦 Uninstalling ait package..."
    pip uninstall -y ai-terminal

    echo "🗑️ Removing virtual environment..."
    deactivate
    rm -rf .venv
else
    echo "⚠️ No virtual environment found."
fi

echo "✅ Uninstallation complete!"
