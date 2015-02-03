#!/usr/bin/python2.7

# Create the gnuplot script for MO energy diagrams
# (This version will not consider Energy degeneracy any longer.)
# The script is released under MIT license.

# Usage: plotMO.py <datefile>

# Date file structure: 
#	1) different molecules diveded by blank line, 
#	2) for each molecule section, start with molecule name
#	3) (no more needed for this version)second line for HOMO number
#	4) rest of section are energys, 1 MO per line, at least 2 colonm (<#MO> <MO_energy> [color])

# First version finish time: 2015.01.05
# Written by Chang Liu

# <2015.01.10>
# Change the unit of plot from Hartree to eV.

# <2015.02.03>
# Make a new version, without degenerance, the code read much better than before.
# Thanks to Kushal's gnuplot script gives me some better idea :D


# import modules
import sys

# print header
def printHeader():
	print """#################################
# Plot MO energy diagrams of molecular
# Created by plotMO.py
# Written by Chang Liu(cliu18@ncsu.edu)
#################################
		
set term postscript enhanced color solid font "Helvetica"
		
		
set ytics nomirror font "Helvetica, 20"
set ylabel "Energy [eV]" font "Helvetica, 20" offset -1,0
		
set noxtics
set nokey

"""



# print arrow
def printArrow(info, left, right):
	commet = info[0]
	energy = float(info[1])
	try:
		color = info[2]
	except:
		color = "black"
	
	print " ### %s ### " % commet
	print """set arrow from %f,%f to %f, %f nohead lc rgb "%s" linewidth 1.""" % (float(left), energy, float(right), energy, color)
	return




# def the main function
def main():
	if len(sys.argv) < 2:
		print """Usage: plotMO.py <datefile> > <script>"""
		exit(0)
	
	name = ""
	for char in sys.argv[1]:
		if char == '.':
			break

		name+=char
	
	Hartree2eV = 27.2113850560

	try:
		datefile=open(sys.argv[1], 'r')
		inputTemp=datefile.read().splitlines()
		datefile.close()
		printHeader()
		print 'set output "%s.eps" ' % name
	except:
		sys.exit("ERROR. No such date file")
	
	molName = []	# name of molecules
	molCount = 0	# count fo molecules
	HOMOnum = []	# number of HOMO
	MOenergys = []	# energy for MOs(as well as color) (final it will be 2 dimensional)
	newSection=True	# whether star a new section
	maxE = -9999999.# max energy value
	minE = 9999999.	# min energy value
	
	# treat the input data.
	for line in inputTemp:
		line = line.strip()
		# blank lines means new section
		if line=="":
			newSection=True
			continue
		# set new molecule name	
		if newSection:
			molName.append(line)
			molCount = molCount + 1
			newSection = False
			MOenergys.append([])
			#print molName[molCount-1]
			continue
		# get MO energy
		Currlevel = line.split()
		Currlevel[1] = float(Currlevel[1]) * Hartree2eV
		maxE = max(maxE, Currlevel[1])
		minE = min(minE, Currlevel[1])
		MOenergys[molCount-1].append(Currlevel)
	
	# beginning write script
	
	# set x range 
	maxX = 100 * molCount
	print "set xrange [0:%f]" % maxX
	
	# set y range
	energySpan = maxE - minE
#print maxE
#print minE
	expandE = energySpan * 0.05
	print "set yrange [%f:%f]" % (minE-expandE, maxE+expandE)
	

	# print the label
	print """set xtics nomirror font "Helvetica, 16" out 2,2,6 ( \\"""
	for mol in range(molCount):
		diaCenter = 50 + 100 * mol
		if (mol != molCount - 1):
			print """ "%s" %f , \\""" % (molName[mol], diaCenter)
	else:
			print """ "%s" %f ) \\""" % (molName[mol], diaCenter)
	print ""

	# plot energy level
	for mol in range(molCount):
		print """#<<<<<<<<<< %s >>>>>>>>>>#""" % molName[mol]
		for level_info in MOenergys[mol]:

			diaCenter = 50 + 100 * mol
			barLeft = diaCenter - 40
			barRight = diaCenter + 40

			printArrow(level_info, barLeft, barRight)
			
		print ""

	# plot the diagram
	print ""
	print "plot NaN"



if __name__=='__main__':
	main()
	exit(0)
