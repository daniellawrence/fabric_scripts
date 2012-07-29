#!/usr/bin/env python
from fabric.api import *

@task()
def uptime():
	""" print the uptime
	"""
	run("uptime")
