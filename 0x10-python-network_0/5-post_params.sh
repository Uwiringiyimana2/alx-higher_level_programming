#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response 
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
