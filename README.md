# dx2push
Takes a mail message from dxmaps and sends the useful pieces via pushover. This is designed to be passed an email via something like **/etc/maildroprc** like this:

```bash
if (/^Subject: Possible Sporadic-E/)
{
   cc "|/usr/local/bin/dx2push.py"
}
```
## Prerequisites

You'll need to have an account at [pushover.net](https://pushover.net/). You'll also need to either use an existing [pushover app ID or create a new one](https://pushover.net/apps).

## Dependencies

```python
import re
import sys
import configparser
from chump import Application
```
## Configuration
Edit dx2push.ini to add your app and user credentials, then copy it to /usr/local/etc (or a similar directory; you'll need to update the code.)

## Test
Feed an existing email in by running 
```bash
/path/to/dx2push.py < sample
```
