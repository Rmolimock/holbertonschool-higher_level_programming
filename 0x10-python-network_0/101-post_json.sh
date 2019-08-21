#!/bin/bash
# send a POST request with the contents of a variable, declared as a JSON file
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
