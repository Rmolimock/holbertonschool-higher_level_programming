#!/bin/bash
# display size of body of response in bytes
curl -sw "\n%{size_download}\n" $1 | tail -1
