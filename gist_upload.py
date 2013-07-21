import os
import sys

import subprocess


try:
	filename = sys.argv[1]

except:
	print "Syntax: {} file".format(sys.argv[0])
	print "Uploads file to gist.github.com"
	sys.exit(1)


command = "gist {}".format(filename)

print "Running %s" % command
url = subprocess.check_output(command)

print url
