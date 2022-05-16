from flask import Flask, make_response
from markupsafe import escape
from ics import Calendar, Event
from datetime import timedelta, datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p> Hello, World </p>'

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/domani')
def domani():
    domani = datetime.now() + timedelta(days=1)
    c = Calendar()
    e = Event()
    e.name = "Ci aggiorniamo Domani"
    e.begin = domani
    e.end = domani + timedelta(hours=1)
    c.events.add(e)
    c.events
    r = make_response(str(c))
    r.headers["Content-Disposition"] = "attachment; filename=domani.ics"
    return r
