#!/bin/bash
# sends a request to that URL, and displays the size of the body of the response 
curl -s -o /dev/null -w "%{http_code}" "$1"
