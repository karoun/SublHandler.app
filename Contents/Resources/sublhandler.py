#!/usr/bin/python

DEBUG = False

import sys
import logging
from urlparse import parse_qs
from os.path import exists, expanduser, isdir
from subprocess import call

if DEBUG:
    logging.basicConfig(filename='/tmp/sublhandler.log', filemode='w+', level=logging.DEBUG)

if len(sys.argv) != 2:
    logging.error('Wrong # of arguments')
    sys.exit(1)

pythonFile, url = sys.argv
prefix, _, query = url.partition('?')

if not query:
    logging.error('Could not find querystring')
    logging.info(url)
    sys.exit(1)

params = parse_qs(query)

if not params:
    logging.error('Could not parse querystring')
    logging.info(query)
    sys.exit(1)

if not params.get('url', False):
    logging.error('No URL was passed')
    logging.info(params)
    sys.exit(1)

fileName = params['url'][0]
logging.info(fileName)
if fileName.startswith('file://'):
    fileName = fileName[7:]

fileName = expanduser(fileName)

if not exists(fileName):
    logging.error(fileName + ' does not exist')
    logging.info(params)
    sys.exit(1)

if not isdir(fileName):
    line = int(params.get('line', [1])[0])
    column = int(params.get('column', [1])[0])
    fileName += ':%d:%d' % (line, column)

call(['subl', fileName])
