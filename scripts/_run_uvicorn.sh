#!/bin/bash
# uvicorn 'main:app' --host '0.0.0.0' --port '80' &

APP='main:app'
HOST='0.0.0.0'
PORT='443'
CERT='/etc/letsencrypt/live/qwality.fun/cert.pem'
KEY='/etc/letsencrypt/live/qwality.fun/privkey.pem'

uvicorn $APP --host $HOST --port $PORT --ssl-keyfile $CERT --ssl-certfile $KEY