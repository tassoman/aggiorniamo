#!/bin/sh
. env/bin/activate
export FLASK_APP=app
flask run \
	>/dev/null \
	2>&1 &

