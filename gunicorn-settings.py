#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from playground import settings

bind = '127.0.0.1:8'+str(os.getuid())[1:]
workers = 2
#worker_class = 'eventlet'
#max_requests = 2048
pidfile = settings.rootrel('logs/django.pid')
user = settings.playground
group = settings.playground
logfile = settings.rootrel('logs/gunicorn.log')
#loglevel = 'info'
proc_name = 'gunicorn-'+settings.playground
