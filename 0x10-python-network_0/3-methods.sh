#!/bin/bash
# Display all Http methods of a server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
