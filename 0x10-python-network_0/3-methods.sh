#!/bin/bash
# display allowed methods in HTTP Header
curl -sI "$1" | grep "Allow:" | cut -d " " --complement -f 1
