#!/usr/bin/env python

import re
import sys
import configparser
from chump import Application

inBody = False
Body =""

# Read in the app token & user key

config = configparser.ConfigParser()
config.read('/usr/local/etc/dx2push.ini')
myToken = config['keys']['token']
myUser = config['keys']['user']

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
   
app = Application(myToken)
#TODO app.is_authenticated should be True

user = app.get_user(myUser)
#TODO make aure user.is_authenticated = True

message = user.create_message( 
    title=Subject, 
    message=Body 
    )

message.send()
