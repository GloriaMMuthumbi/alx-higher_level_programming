#!/bin/bash
#sends request to URL passed and displays the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
