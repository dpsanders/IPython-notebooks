import os
import sys

try:
	notebook_file = sys.argv[1]

except:
	print "Syntax: {} notebook_file".format(sys.argv[0])
	sys.exit(1)


command = 'ipython nbconvert --format="python" {}'.format(notebook_file)
print "Running", command
os.system(command)

basename = os.path.basename(notebook_file)

run_command = 'python {}'.format(basename)
os.system(run_command)




