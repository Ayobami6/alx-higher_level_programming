#!/bin/bash
# Sends a request to an endpoint with an header variable
curl -sH "X-School-User-Id: 98" "${1}"
