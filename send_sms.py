#!/usr/bin/env python3

import boto3

client = boto3.client('sns')

# Publish a message.
client.publish(Message="Good news everyone!",
                 TopicArn="arn:aws:sns:us-east-1:292915697840:waterpi")