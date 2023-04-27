#!/bin/bash
# get size of http response in bytes
curl -s "$1" | wc -c
