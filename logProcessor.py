#!/usr/bin/python

import decimal
import sys
import indexProp
import os 


urlIndex=6
statusCodeIndex=8
requestTimeIndex=15

## initializing.
if len(sys.argv) != 3:
	print "wrong parameters, using  'command  srcFile destFile'"
	exit(1)

srcFile = sys.argv[1]
destFile = sys.argv[2]
logfile = open(srcFile,"rb")
analysisfile = open(destFile,"w")

## pre-processing
os.system("wc -l "+ srcFile)

## start processing 
dic = {}
count = 0
for line in logfile:
	try:
		arr = line.split(" ")
		#method=  arr[6]
		url= str(arr[urlIndex])
		if url.find("\'") > 0 or url.find("\"") >0:
			continue
		if url.find("?") >0:
			url= url[:url.find("?")]
		statusCode= arr[statusCodeIndex]
		#contentLength= arr[10]
		requestTime= decimal.Decimal(arr[requestTimeIndex])


		if url in dic :
			dic[url]["count"]+=1
			dic[url]["rt"] += requestTime
		else :
			dic[url] = {"count":1,"rt":requestTime}

		count+=1
		if count % 10000 == 0:
			print count
	except Exception,e :
		print e
		print line 
		continue

## post-process
for k,v in dic.items():
	v["rt"]=str(v["rt"])

## other stuff
analysisfile.write(str(dic))
logfile.close()
analysisfile.close()
