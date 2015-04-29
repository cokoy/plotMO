#!/usr/bin/env python
'''
To seperate Gaussian log file with with multistep calculation
Userage : seperate_log.py logfile1 logfile2 ...
Created by Chang Liu @ Apr.29.2015
'''
import sys

def seperate_file(filename):
	try:
		logfile=open(filename, 'r')
		inputTemp=logfile.read().splitlines()
		logfile.close()
	except:
		print "No such file: %s" % filename
		return
	
	outNUM=0
	outName="%d_%s" % (outNUM, filename)
	outfile=open(outName, "w")
	
	for line in inputTemp:
		outfile.write("%s\n"%line)
		if "Normal term" in line:
			outfile.close
			outNUM += 1
			outName="%d_%s" % (outNUM, filename)
			outfile=open(outName, "w")



if __name__=="__main__":
	for filename in sys.argv[1:]:
		seperate_file(filename)
	exit(0)

