#!/usr/bin/env python

import re
import sys
from chump import Application

myToken = 'aacbdwqqnw1ck1dprtwmhyn9xf75j8'
myUser = 'u5fiaqin56on6nbmkrckqehbxxwj3u'
inBody = False
Body =""

for line in sys.stdin: #fileinput.input():
    if re.match('^\\s*$',line):
        inBody = True
    if inBody:
        Body=Body+line
    elif re.match('^Subject:',line ):
        Subject=line
    elif re.match('^\\s*You receive',line):
        break

app = Application(myToken)
#TODO app.is_authenticated should be True

user = app.get_user(myUser)
#TODO make aure user.is_authenticated = True

message = user.create_message( 
    title=Subject, 
    message=Body 
    )

message.send()
