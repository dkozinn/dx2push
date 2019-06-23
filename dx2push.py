#!/usr/local/share/python/pyenv/shims/python3

import re
import sys
import configparser
from chump import Application

inBody = False
Body = ""
Subject = ""

# Read in the app token & user key

try:
    config = configparser.ConfigParser()
    config.read('/usr/local/etc/dx2push.ini')
    myToken = config['keys']['token']
    myUser = config['keys']['user']
except KeyError as e:
    exit("Unable to parse config file")

# This assumes the the interesting stuff is all before the line that starts with the string in the 
# first re.match() test. Obviously this can break.
# TODO Find a better way to do this

for line in sys.stdin:
    if inBody:
        if re.match('^\\s*You receive',line):
            break
        else:
            Body=Body+line
    elif re.match('^Subject:',line ):
        Subject=line
    elif re.match('^\\s*$',line):
        inBody = True

# Make sure we got at least a subject or a body
if (not inBody and not Subject):
    exit("Empty email message")
   
app = Application(myToken)
if not app.is_authenticated:
    exit("Unable to authenticate pushover application")

user = app.get_user(myUser)
if not user.is_authenticated:
    exit("Unable to authenticate pushover user")

message = user.create_message( 
    title=Subject, 
    message=Body,
    sound="cosmic"
    )

if not message.send():
    exit("Error sending message")
