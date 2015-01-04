#!/usr/bin/python2.7

# Create the gnuplot script for MO energy diagrams
# Usage: plotMO.py <datefile> > <script>
# Date file structure: 
#	1) different molecules diveded by blank line, 
#	2) for each molecule section, start with molecule name
#	3) second line for HOMO number
#	4) rest of section are energys, 1 MO per line
# Update time: 2015.01.02
# Written by Chang Liu


# import modules
import sys


# print arrow
def printArrow(energy, left, right, lineshape, commet):
	print commet
	print """set arrow from %f,%f to %f, %f nohead lc %d linewidth 1.""" % (float(left), energy, float(right), energy, lineshape)
	return


# print arrows for degenarated energys
def putDegMO(diaCenter, degEnergy, degStyl, degType):
	
	deg = len(degEnergy)
	# get the HOMO energy
	for i in range(deg):
		if degStyl[i] == 1:
			eHOMO = degEnergy[i]
		else:
			eHOMO = 0
	
	# calc the width of line and where to put them
	if deg <= 3:
		unitLen = 30.
		unitMarg = 5.
		start = diaCenter - (unitLen * deg)/2.	
	else:
		unitLen = 90. / deg
		unitMarg = unitLen / 6.
		start = diaCenter - 45.
		
	barLen = unitLen - 2 * unitMarg
	
	# change the lineshape for different energies as well HOMO
	currlc = 2
	for i in range(deg-1):
		if degEnergy[i] == eHOMO:
			degStyl[i] = 1
		elif degEnergy[i] != degEnergy[i+1]:
			currlc = currlc + 1
		
		degStyl[i+1] = currlc
		
	# start output
	left = start + unitMarg
	for i in range(deg):
		right = left + barLen
		printArrow(degEnergy[i], left, right, degStyl[i], degType[i])	
		left = left + unitLen
		
	return



# def the main function
def main():
	if len(sys.argv) < 2:
		print """Usage: plotMO.py <datefile> > <script>"""
		exit(0)
	
	# set tolerance for degenerate (for plot only, 
	# if energy are not exact the same, will use different color
	degToler = 0.001
	if len(sys.argv) > 3:
		degToler=float(sys.argv[2])
	
	try:
		datefile=open(sys.argv[1], 'r')
		inputTemp=datefile.read().splitlines()
		datefile.close()
	except:
		sys.exit("ERROR. No such date file")
	
	molName = []	# name of molecules
	molCount = 0	# count fo molecules
	HOMOnum = []	# number of HOMO
	MOenergys = []	# energy for MOs (final it will be 2 dimensional)
	newSection=True	# whether star a new section
	getHOMO=False	# This date is homo number?
	maxE = -9999999.# max energy value
	minE = 0.0		# min energy value
	
	# treat the input data.
	for line in inputTemp:
		# blank lines means new section
		if line=="":
			newSection=True
			continue
		# set new molecule name	
		if newSection:
			molName.append(line)
			molCount = molCount + 1
			getHOMO = True
			newSection = False
			MOenergys.append([])
			#print molName[molCount-1]
			continue
		# get number of HOMO
		if getHOMO:
			HOMO=int(float(line))
			HOMOnum.append(HOMO)
			getHOMO = False
			#print HOMOnum[molCount-1]
			continue
		# get MO energy
		energy = float(line)
		maxE = max(maxE, energy)
		minE = min(minE, energy)
		MOenergys[molCount-1].append(energy)
	
	# beginning write script
	
	# set x range 
	maxX = 100 * molCount
	print "set xrange [0:%f]" % maxX
	
	# set y range
	energySpan = maxE - minE
	expandE = energySpan * 0.05
	print "set yrange [%f:%f]" % (minE-expandE, maxE+expandE)
	
	bottomLabel = minE - expandE* 1.5
	
	for mol in range(molCount):
		# print the label first
		diaCenter = 50 + 100 * mol
		print """\nset label "{%s}" at  %d, %f center """ % (molName[mol], diaCenter, bottomLabel)
		
		# sort the energies
		MOenergys[mol].sort()
		
		# start out put diagrams
		level = 0
		degEnergy = []
		degStyl = []
		degType = []
		degStat = False
		barLeft = diaCenter - 10
		barRight = diaCenter + 10
		
		for energy in MOenergys[mol]:
			
			if (level + 1) == HOMOnum[mol]:
				lineStyl = 1
				MOtype = "##### HOMO #####"
			else:
				lineStyl = 2
				if (level + 1) < HOMOnum[mol]:
					MOtype = ("##### HOMO-%d #####" % (HOMOnum[mol] - level - 1))
				elif level == HOMOnum[mol]:
					MOtype = "##### LUMO #####"
				else:
					MOtype = ("##### LUMO+%d #####" % (level - HOMOnum[mol]))
			
			if level + 1 < len(MOenergys[mol]):
				#print "%f,  %f " % (energy, MOenergys[mol][level+1])
				
				if abs(energy - MOenergys[mol][level+1]) < degToler: #degenerate
					degEnergy.append(energy)
					degStyl.append(lineStyl)
					degType.append(MOtype)
					DegStat = True
				
				elif DegStat: #end of degenerate, start output 
					degEnergy.append(energy)
					degStyl.append(lineStyl)
					degType.append(MOtype)
					
					putDegMO(diaCenter, degEnergy, degStyl, degType)
					
					DegStat = False
					degEnergy = []
					degStyl = []
					degType = []
					
				
				else: 
					printArrow(energy, barLeft, barRight, lineStyl, MOtype)
			
			
			elif DegStat:
				degEnergy.append(energy)
				degStyl.append(lineStyl)
				degType.append(MOtype)
				
				putDegMO(diaCenter, degEnergy, degStyl, degType)
				
				DegStat = False
				degEnergy = []
				degStyl = []
				degType = []
			
			
			else: 
				printArrow(energy, barLeft, barRight, lineStyl, MOtype)
				
				
			level = level + 1



if __name__=='__main__':

# print the header of gnu file
	print """#################################
# Plot MO energy diagrams of molecular
# Created by plotMO.py
# Written by Chang Liu(cliu18@ncsu.edu)
#################################

set term postscript enhanced color solid font "Helvetica"
set output "MO.ps"

set ylabel "{E_{orbital}} [Hartree}]" font "Helvetica,15" offset 1,-0.5
set noxtics
set nokey

set bmargin 2.5
set lmargin 9
	"""

	main()

	# plot the diagram
	print ""
	print "plot NaN"

	exit(0)
