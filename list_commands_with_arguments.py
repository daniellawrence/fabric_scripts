#!/usr/bin/env python
"""
Loop over everything in the fabfiles.py direct, looking for WrappedCallableTask, 
for every single WrappedCallableTask that is found.
This will not execute the tasks, only display information about them
"""

# Used so that we can call api.host_string to set it to the localhost ( for testing )
from fabric import api

# use the sys.argv to get the arguments from the command line
from sys import argv

# store the 1st argument as module_name
module_name = argv[1]

# remove the '.py' from the module name, for importing reasons
module_name = module_name.replace('.py','')

# import the local tasks that are all located fabfiles.
fabfile_tasks = __import__(module_name)

# in this example, we are going to connect to the localhost
api.env.host_string = "localhost"

# loop over all the objects in the fabfiles
for name in fabfile_tasks.__dict__.keys():

	# If the object is not a WrappedCallableTask, then skip over it,
	# we are not interested in it.
	if type(fabfile_tasks.__dict__[name]).__name__ != "WrappedCallableTask":
		continue

	# Take the name of the task and create a new placeholder for the object
	# called task.
	task = fabfile_tasks.__dict__[name]

	# this is some varible changes, only so the printf style print is able to work
	task.module_name = module_name
	task.co_varnames = task.func_code.co_varnames
	task.co_argcount = task.func_code.co_argcount
	task.__doc__ = task.__doc__.strip()

	if task.__dict__['co_argcount'] == 0:
		# print the name of the task, and the docstring
		print "[%(module_name)s.%(name)s]\t%(__doc__)s" % ( task.__dict__ )
	else:
		# print the name of the task, and the docstring. Also print how many argument
		# the function is expecting, and by what name
		print "[%(module_name)s.%(name)s]\t%(__doc__)s requires(%(co_argcount)s): %(co_varnames)s " % ( task.__dict__ )
