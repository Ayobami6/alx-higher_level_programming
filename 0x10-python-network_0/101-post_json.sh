#!/bin/bash
# sends a post request to an endpoint with jso file
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
