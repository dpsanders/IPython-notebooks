#!/usr/bin/env python

'''
Syntax: run_ipynb notebook.ipynb

Runs the Python code contained in an IPython notebook.
'''


import os
import sys
import subprocess

try:
	notebook_file = sys.argv[1]

except:
	print "Syntax: {} notebook.ipynb".format(sys.argv[0])
	sys.exit(1)


command = ['ipython', 'nbconvert', '--format="python"', notebook_file]
print "Running", command
subprocess.call(command)

basename, ext = os.path.splitext(notebook_file)

script_name = basename + '.py'

print script_name				

# nbconvert puts the script inside the nbconvert_build directory
# Get it out of there!:
command = ['mv', 'nbconvert_build/%s' % script_name, '.']
print command
subprocess.check_call(command)

# It fails to strip out the IPython magics
# Get rid of them:
# [Would be easier to use awk for this:

# awk 'substr($0,1,1) != "%"' 

script_contents = open(script_name, "r").readlines()
lines = [line for line in script_contents if line[0] != "%"]
script_contents = ''.join(lines)

print script_contents

# Output the script back into the same file:

output = open(script_name, "w")
output.write(script_contents)

# Run the resulting Python script:

command = ['ipython', 'script_name']


execfile(script_name)
				



