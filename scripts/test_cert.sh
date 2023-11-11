#!/bin/bash

echo "$1" > /home/cv/static/.well-known/acme-challenge/test-file.txt
curl http://www.qwality.fun/.well-known/acme-challenge/test-file.txt
