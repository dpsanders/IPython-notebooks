#!/usr/bin/env python
"""
Uses the `gist` function (install with `gem install gist`)
to create a new gist, whose URL it prints.

If the file is an .ipynb (IPython notebook document)
then it also prints the relevant nbviewer URL.
"""

import os
import sys

import subprocess


try:
	filename = sys.argv[1]

except:
	print "Syntax: {} file".format(sys.argv[0])
	print "Uploads file to gist.github.com"
	sys.exit(1)


command = ["gist", filename]

#print "Running %s" % command
gist_url = subprocess.check_output(command)

print "New gist located at:"
print gist_url

basename, extension = os.path.splitext(notebook_file)
#print "Extension ", extension

is_IPython_notebook = (extension == ".ipynb")

if (is_IPython_notebook):
	gist_url_parts = os.path.split(gist_url)
	gist_identifier = gist_url_parts[-1]

	nbviewer_url = r"http://nbviewer.ipython.org/" + gist_identifier

	print "View your notebook at:"
	print nbviewer_url 