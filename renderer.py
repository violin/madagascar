#!/usr/bin/python

import sys

## initializing.
if len(sys.argv) != 2:
	print "wrong parameters, using  'command  srcFile '"
	exit(1)

file= open(sys.argv[1],"r")
content = file.read()
content = content.replace('\'','\"')

# file.close()
filew = open(sys.argv[1],"w")
filew.write("showResult(\'" +content +"\')")
filew.close()
