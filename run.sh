#!/bin/sh
. env/bin/activate
export FLASK_APP=app
export FLASK_ENV=development
flask run

#flask run \
#	>/dev/null \
#	2>&1 &

