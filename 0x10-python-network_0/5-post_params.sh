#!/bin/bash
# Scripts that sends and email to an endpoint
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
