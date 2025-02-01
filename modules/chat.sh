#!/bin/bash

CHAT_HISTORY=""

function ai_chat() {
    local user_message="$1"
    local tone="$2"
    local mode="$3"
    local voice="$4"

    CHAT_HISTORY="$CHAT_HISTORY\nUser: $user_message"

    case "$tone" in
        "friend") tone_instruction="You are my friendly companion, always positive and supportive." ;;
        "officer") tone_instruction="You are a polite and professional officer, giving serious and direct responses." ;;
        "dev") tone_instruction="You are a developer, offering helpful and technical insights." ;;
        *) tone_instruction="You are a helpful assistant, engaging in a neutral conversation." ;;
    esac

    response=$(ollama run "$MODEL" "Chat with me. You are $tone_instruction. Remember the entire conversation so far: $CHAT_HISTORY")

    CHAT_HISTORY="$CHAT_HISTORY\nAI: $response"

    if [[ "$mode" == "speak" ]]; then
        if [[ -n "$voice" ]]; then
            say -v "$voice" "$response"
        else
            say "$response"
        fi
    else
        echo -e "\n$YELLOW($tone)$RESET $ORANGE AI : $GREEN$response$RESET\n"
    fi
}

function start_ai_chat() {
    local tone=$1
    local mode=$2
    local voice=$3
    echo "Entering AI Chat Mode as $tone. Type '/exit/chat' to return to the terminal."

    while true; do
        echo -e -n "$YELLOW($tone)$RESET $BLUE YOU : $YELLOW $RESET"
        read user_input

        if [[ "$user_input" == "/exit/chat" ]]; then
            echo "Exiting AI Chat Mode."
            break
        else
            ai_chat "$user_input" "$tone" "$mode" "$voice"
        fi
    done
}
