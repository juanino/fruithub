#!/usr/bin/env python3

import sys
try:
    import config as cfg
except:
    print("could not find config file")
    print("copy config_sample.py to config.py and adjust")
    sys.exit(1)

from markupsafe import escape

from flask import Flask
app = Flask(__name__)

import boto3
client = boto3.client('sns')

@app.route('/')
def hello_world():
    return 'Main page checks out'

@app.route('/checkin/<devicename>')
def checkin(devicename):
    return 'fruithub: Device %s checkin works' % escape(devicename)

@app.route('/post/<devicename>/<sensor>/<status>')
def store_sensor(devicename,sensor,status):
    # Publish a message.
    msg ='fruithub: Device:' + devicename + ' sensor:' + sensor + ' has status:' + str(status) 
    client.publish(Message=msg, TopicArn=cfg.topic_arn)
    return msg
