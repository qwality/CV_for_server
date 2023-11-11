#!/bin/bash
# uvicorn 'main:app' --host '0.0.0.0' --port '80' &

# APP='main:app'
# HOST='0.0.0.0'
# PORT='443'
# CERT='/etc/letsencrypt/live/qwality.fun/cert.pem'
# KEY='/etc/letsencrypt/live/qwality.fun/privkey.pem'

uvicorn main:app --host 0.0.0.0 --port 443 --ssl-keyfile $SSL/privkey.pem --ssl-certfile $SSL/fullchain.pem &

# uvicorn $APP --host $HOST --port $PORT --ssl-keyfile $CERT --ssl-certfile $KEY

# uvicorn main:app --host 0.0.0.0 --port 443 --ssl-keyfile /etc/letsencrypt/live/qwality.fun/fullchain.pem --ssl-certfile /etc/letsencrypt/live/qwality.fun/privkey.pem