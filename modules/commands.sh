#!/bin/bash

function get_command() {
    local input_text="$1"
    
    # Generate the prompt to get the appropriate Bash command from the model
    response=$(ollama run "$MODEL" "Imagine you are a terminal expert. When I ask a question or give an instruction, provide the exact and correct Bash command. If there's any error in the input, fix it. Only return the Bash command, no additional explanation or extra text. Input: '$input_text'")

    # Remove any extra formatting or undesired text (such as markdown)
    clean_command=$(echo "$response" | sed -E 's/```bash//g' | sed -E 's/```//g' | xargs)

    echo "$clean_command"
}

fdasfas
