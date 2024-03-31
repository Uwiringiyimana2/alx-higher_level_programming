#!/usr/bin/bash
# sends a request to that URL, and displays the size of the body of the response 
curl -sI $1 | grep "Allow" | cut -d " " -f 2-
