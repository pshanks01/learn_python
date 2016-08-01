#!/bin/python

from base64 import encodestring, decodestring
from base64 import urlsafe_b64encode
from sys import argv

script, url = argv

assert isinstance(url, basestring)
print urlsafe_b64encode(url)
