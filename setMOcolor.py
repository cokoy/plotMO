#!/usr/bin/python2.7

# Help user select MO range and set color
# The script is released under MIT license.

# Usage: setMOcolor.py <glog2MOinfo.py outputfile> <start energy in Hartree> <end energy in Hartree>
#						[color:orbit1,orbit2...] [color:orbit_1:orbit_n]

# Input structure
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


# Output structure
#	|								|
# 1 | <Name of log file>			|
# 2 | #MOn    Energy    color/blank	|
# 3 | #MOn+1  Energy    color/blank	|
# 4 | #MOn+2  Energy    color/blank	|
#...| ...     ...        ...		|


# Date of creation: 2015.02.04
# Created by: Chang Liu


# import modules
import sys


def main():
	if len(sys.argv)<4:
		print """setMOcolor.py <glog2MOinfo.py outputfile> <start energy in Hartree> <end energy in Hartree>
[color:orbit_a,orbit_m-orbit_n,...]"""
		exit(0)

	fname = sys.argv[1]
	try:
		datefile=open(fname, 'r')
		inputTemp=datefile.read().splitlines()
		datefile.close()
	except:
		sys.exit("ERROR. No such log file")

	print inputTemp[0]
	colorRec = (len(inputTemp))*[""]
	# get the energy range
	minE = min(float(sys.argv[2]), float(sys.argv[3]))
	maxE = max(float(sys.argv[2]), float(sys.argv[3]))
	
	# get color info
	if len(sys.argv) > 4:
		for colorArg in sys.argv[4:]:
			# slipt color and energy levels argument
			(color, orbitL) = colorArg.split(":")
			# slipt different energy level range
			orbitR = orbitL.split(",")
			# treat with different range
			for orbit in orbitR:
				level = orbit.split("-")
				if len(level) == 1:
					colorRec[int(level[0])] = color
				else:
					for i in range(int(level[0]), int(level[1])+1):
						colorRec[i] = color

	for line in inputTemp[1:]:
		MOinfo = line.split()
		# select those MO in energy range
		if float(MOinfo[1]) < minE:
			continue
		if float(MOinfo[1]) > maxE:
			break
		line = line.replace("occ", colorRec[int(MOinfo[0])])
		line = line.replace("virt", colorRec[int(MOinfo[0])])
		line = line.replace("HOMO", colorRec[int(MOinfo[0])])
		print line

	print 5*""

if __name__=='__main__':
	main()
	exit(0)
