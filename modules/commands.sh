#!/bin/bash

function get_command() {
    local input_text="$1"
    
    response=$(ollama run "$MODEL" "Convert the following natural language input into a valid Bash command. Provide only the command, no extra text also if any error in the text correct it: $input_text")

    # Remove triple backticks and extra text
    clean_command=$(echo "$response" | sed -E 's/```bash//g' | sed -E 's/```//g' | xargs)

    echo "$clean_command"
}
