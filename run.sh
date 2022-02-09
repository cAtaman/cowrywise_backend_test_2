#!/usr/bin/bash

#run side by side
if [[ $# -eq 0 ]]; then
    echo "Enter the client port followed by the admin port"
    exit 1
fi

CLIENT_PORT=$1
ADMIN_PORT=$2

export FLASK_APP=src.admin.wsgi:app
flask run --host 0.0.0.0 --port $((ADMIN_PORT)) &

export FLASK_APP=src.client.wsgi:app
flask run --host 0.0.0.0 --port $((CLIENT_PORT)) &

# run combined
#python3 -m werkzeug.serving -b 0.0.0.0:1759 -rd app:application
