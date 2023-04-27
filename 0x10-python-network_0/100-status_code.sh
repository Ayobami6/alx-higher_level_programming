#!/bin/bash
# request for a status code 
curl -s -o /dev/null -w "%{http_code}" "$1"
