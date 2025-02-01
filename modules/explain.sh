#!/bin/bash

function explain() {
    local input="$1"

    if [[ -f "$input" ]]; then
        file_content=$(cat "$input")
        explanation=$(ollama run "$MODEL" "Explain the following content in simple terms: $file_content")
        echo -e "\nExplanation of file $input:\n$explanation\n"
    else
        explanation=$(ollama run "$MODEL" "Explain the following question in simple terms: $input")
        echo -e "\nExplanation:\n$explanation\n"
    fi
}
