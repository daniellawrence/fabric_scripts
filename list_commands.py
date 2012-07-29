#!/usr/bin/env python
"""
Loop over everything in the fabfiles.py direct, looking for WrappedCallableTask, 
for every single WrappedCallableTask that is found, execute the task on the localhost
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

	# print the name of the task, and the docstring
	print "[%(name)s]\t%(__doc__)s" % ( task.__dict__ )

	# Run the task
	task()
