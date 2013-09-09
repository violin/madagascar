#!/usr/bin/python

import sys
import decimal


def mergeAnalysisDic(src, dest):
	dest['count'] += src['count']
	dest['rt'] = str(decimal.Decimal(dest['rt'])+decimal.Decimal(src['rt']))
	return dest
	

## initializing.
if len(sys.argv) < 4:
	print "wrong parameters, using  'command  file...'"
	exit(1)

filenames = sys.argv[2:-1]
destFileName = sys.argv[-1]
files = []
dicList =[]

for filename in filenames:
	file = open(filename,'r')
	files.append(file)
	dicList.append(file.read())

result = eval(dicList[0])

for dicstr in dicList:
	dic = eval(dicstr)
	for key in dic:
		if key in result:
			mergeAnalysisDic(dic[key],result[key])
		else:
			result[key] = dic[key]

outputFile = open(destFileName,'w')
outputFile.write(str(result))

outputFile.close()
for fileitem in files:
	fileitem.close()




