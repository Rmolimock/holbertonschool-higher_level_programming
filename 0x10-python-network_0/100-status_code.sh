#!/bin/bash
# display status code of curl response without pipes or redirect
curl -so /dev/null -w "%{http_code}" $1
