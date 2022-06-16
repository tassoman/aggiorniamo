from flask import Flask, make_response
from markupsafe import escape
from ics import Calendar, Event
from datetime import timedelta, datetime, time
import pytz

tz_ita = pytz.timezone('Europe/Rome')

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Ci Aggiorniamo...'

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/domani')
@app.route('/domani/')
@app.route('/domani/<path:quando>')
def domaniQuando(quando=None):
    if quando == 'mattina':
        hours = timedelta(hours=10)
    elif quando == 'pomeriggio':
        hours = timedelta(hours=14)
    else:
        hours = timedelta(hours=9)

    if escape(quando) != 'None':
        inizio = datetime.combine(
            datetime.now(tz=tz_ita) + timedelta(days=1), 
            time(0,0)
        ) + hours
    else:
        inizio = datetime.now(tz=tz_ita) + timedelta(days=1)

    c = Calendar()
    e = Event()
    e.name = "Ci aggiorniamo Domani"

    if escape(quando) != 'None':
        e.name = e.name + ', ' + escape(quando)

    e.begin = inizio
    e.end = inizio + timedelta(hours=1)
    c.events.add(e)
    c.events
    r = make_response(str(c))
    r.headers["Content-Disposition"] = "attachment; filename=ci-aggiorniamo.ics"
    return r
