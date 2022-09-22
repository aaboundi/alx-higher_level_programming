#!/bin/bash
# Displays the size of the body of a response from a URL
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
