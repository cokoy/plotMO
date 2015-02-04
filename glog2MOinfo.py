#!/usr/bin/python2.7

# Get MO energy information from Gaussian log file.
# The script is released under MIT license.

# Usage: glog2MOinfo.py <gaussian log>

# Output structure
#	|								|
# 1 | <Name of log file>			|
# 2 | #MO1    Energy1    occ		|
# 3 | #MO2    Energy2    occ		|
# 4 | #MO3    Energy3    occ		|
#...| ...     ...        ...		|
# m | #MOm-1  Energym-1  HOMO		|
# n | #MOn-1  Energyn-1  virt		|
#...| ...     ...        ...		|
#	|								|

# Date of creation: 2015.02.04
# Created by: Chang Liu


# import modules
import sys



def main():
	if len(sys.argv)<2:
		print """Usage: glog2MOinfo.py <gaussian log>"""
		exit(0)
	fname = sys.argv[1]
	print "From %s" % fname
	try:
		datefile=open(fname, 'r')
		inputTemp=datefile.read().splitlines()
		datefile.close()
	except:
		sys.exit("ERROR. No such log file")



	# similar to command grep "SCF Done\|Alpha  occ. eigenvalues\|Alpha virt. eigenvalues" FeTpy2_singlet.log
	# find the final occupied orbital energy lines and virtual orbital energy lines.
	for line in inputTemp:
		if "SCF Done" in line:
			occMOLine = []
			virtMOLine = []
		if "Alpha  occ. eigenvalues --" in line:
			occMOLine.append(line.replace("Alpha  occ. eigenvalues --", ""))
		if "Alpha virt. eigenvalues --" in line:
			virtMOLine.append(line.replace("Alpha virt. eigenvalues --",""))

#	for line in occMOLine:
#		print line
#	for line in virtMOLine:
#		print line


	# get energies of Occupied MO
	occMOE=[]
	for line in occMOLine:
		for energy in line.split():
			occMOE.append(float(energy))
	HOMO = len(occMOE)
	occMOE.sort()
	# get energies of virtual MO
	virtMOE=[]
	for line in virtMOLine:
		for energy in line.split():
			virtMOE.append(float(energy))
	virtMOE.sort()
#	print len(occMOE)
#	for energy in occMOE:
#		print energy


	# print out Occupied MO information
	num = 1
	type = "occ"
	for energy in occMOE:
		if num == HOMO:
			type = "HOMO"
		print "%4d %12f %10s" % (num, energy, type)
		num += 1
		type = "occ"
	# print out virtual MO information
	type = "virt"
	for energy in virtMOE:
		print "%4d %12f %10s" % (num, energy, type)
		num += 1



if __name__=='__main__':
	main()
	exit(0)