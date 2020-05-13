#!/usr/bin/env python3

from markupsafe import escape

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Main page checks out'

@app.route('/checkin/<devicename>')
def checkin(devicename):
    return 'fruithub: Device %s checkin works' % escape(devicename)
