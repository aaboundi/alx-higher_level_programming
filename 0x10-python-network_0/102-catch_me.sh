#!/bin/bash
# Follows a URL for it to respond with "You got me!"
curl -s 0.0.0.0:5000/catch_me -X PUT -L -d "user_id=98" -H "You got me!"
