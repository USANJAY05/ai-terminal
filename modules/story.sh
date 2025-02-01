#!/bin/bash

function tell_story() {
    local story_prompt="$1"
    
    response=$(ollama run "$MODEL" "Tell me a short, engaging story based on: $story_prompt. Format it properly for reading in the terminal.")

    echo -e "\n=== Story Time ===\n"
    echo "$response" | fold -s -w 80
    echo -e "\n==================\n"
}
