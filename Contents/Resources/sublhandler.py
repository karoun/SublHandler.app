#!/usr/bin/python

import sys
from urlparse import urlsplit, parse_qs
from os.path import exists, expanduser
from subprocess import call

if len(sys.argv) != 2:
    sys.exit(1)

pythonFile, url = sys.argv
parsed = urlsplit(url)

if not parsed.path:
    sys.exit(1)

fileName = expanduser(parsed.netloc + parsed.path)

if not exists(fileName):
    sys.exit(1)

if fileName[-1] != '/':
    params = parse_qs(parsed.query)
    line = int(params.get('line', [1])[0])
    column = int(params.get('column', [1])[0])
    fileName += ':%d:%d' % (line, column)

call(['subl', fileName])
