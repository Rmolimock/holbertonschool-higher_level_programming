#!/bin/bash
# send a POST request to given URL, along with variables
curl -sX POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
