#!/bin/bash
# Displays the body of a response from a URL : only body of a 200 status code
curl -s "$1" -X GET -L
