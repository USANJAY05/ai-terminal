#!/bin/bash

function print_colored() {
    local color="$1"
    local text="$2"
    echo -e "${color}${text}${RESET}"
}
