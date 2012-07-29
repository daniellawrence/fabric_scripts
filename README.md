fabric_scripts
==============

To run the very basic example of list_commands.py just provide the a file with 
fab tasks as argument 1.

    $ ./list_commands.py uptime.py 
    [uptime]	 print the uptime
    [localhost] run: uptime
    [localhost] out:  14:07:11 up 1 day,  1:14,  3 users,  load average: 1.15, 1.32, 1.53

The above is what the following script would look like.

    #!/usr/bin/env python
    from fabric.api import *
    @task()
    def uptime():
	""" print the uptime
	"""
	run("uptime")

