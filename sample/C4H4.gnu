#################################
# Plot MO energy diagrams of molecular
# Created by plotMO.py
# Written by Chang Liu(cliu18@ncsu.edu)
#################################

set term postscript enhanced color solid font "Helvetica"


set ylabel "{E_{orbital}} [eV}]" font "Helvetica,15" offset 1,-0.5
set noxtics
set nokey

set bmargin 2.5
set lmargin 9
	
set output "C4H4.ps" 
set xrange [0:100.000000]
set yrange [-25.040053:14.653467]

set label "{C_4H_4}" at  50, -25.942178 center 
##### HOMO-14 #####
set arrow from 40.000000,-23.235802 to 60.000000, -23.235802 nohead lc 2 linewidth 1.
##### HOMO-13 #####
set arrow from 40.000000,-17.891486 to 60.000000, -17.891486 nohead lc 2 linewidth 1.
##### HOMO-12 #####
set arrow from 40.000000,-16.217985 to 60.000000, -16.217985 nohead lc 2 linewidth 1.
##### HOMO-11 #####
set arrow from 40.000000,-13.760797 to 60.000000, -13.760797 nohead lc 2 linewidth 1.
##### HOMO-10 #####
set arrow from 40.000000,-13.695490 to 60.000000, -13.695490 nohead lc 2 linewidth 1.
##### HOMO-9 #####
set arrow from 40.000000,-10.492710 to 60.000000, -10.492710 nohead lc 2 linewidth 1.
##### HOMO-8 #####
set arrow from 40.000000,-10.236923 to 60.000000, -10.236923 nohead lc 2 linewidth 1.
##### HOMO-7 #####
set arrow from 40.000000,-9.298130 to 60.000000, -9.298130 nohead lc 2 linewidth 1.
##### HOMO-6 #####
set arrow from 40.000000,-8.345732 to 60.000000, -8.345732 nohead lc 2 linewidth 1.
##### HOMO-5 #####
set arrow from 40.000000,-4.908934 to 60.000000, -4.908934 nohead lc 2 linewidth 1.
##### HOMO-4 #####
set arrow from 40.000000,-1.224512 to 60.000000, -1.224512 nohead lc 2 linewidth 1.
##### HOMO-3 #####
set arrow from 40.000000,2.808215 to 60.000000, 2.808215 nohead lc 2 linewidth 1.
##### HOMO-2 #####
set arrow from 40.000000,3.202780 to 60.000000, 3.202780 nohead lc 2 linewidth 1.
##### HOMO-1 #####
set arrow from 40.000000,3.491221 to 60.000000, 3.491221 nohead lc 2 linewidth 1.
##### HOMO #####
set arrow from 40.000000,3.942930 to 60.000000, 3.942930 nohead lc 1 linewidth 1.
##### LUMO #####
set arrow from 40.000000,4.775598 to 60.000000, 4.775598 nohead lc 2 linewidth 1.
##### LUMO+1 #####
set arrow from 40.000000,5.172884 to 60.000000, 5.172884 nohead lc 2 linewidth 1.
##### LUMO+2 #####
set arrow from 40.000000,7.676332 to 60.000000, 7.676332 nohead lc 2 linewidth 1.
##### LUMO+3 #####
set arrow from 40.000000,8.288588 to 60.000000, 8.288588 nohead lc 2 linewidth 1.
##### LUMO+4 #####
set arrow from 40.000000,12.849216 to 60.000000, 12.849216 nohead lc 2 linewidth 1.

plot NaN
