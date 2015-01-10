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
	
set output "C6H6.ps" 
set xrange [0:100.000000]
set yrange [-24.352421:6.678626]

set label "{C_6H_6}" at  50, -25.057672 center 
##### HOMO-14 #####
set arrow from 40.000000,-22.941919 to 60.000000, -22.941919 nohead lc 2 linewidth 1.
##### HOMO-13 #####
set arrow from 40.000000,-20.041185 to 60.000000, -20.041185 nohead lc 2 linewidth 1.
##### HOMO-12 #####
set arrow from 40.000000,-20.038464 to 60.000000, -20.038464 nohead lc 2 linewidth 1.
##### HOMO-11 #####
set arrow from 40.000000,-16.160842 to 60.000000, -16.160842 nohead lc 2 linewidth 1.
##### HOMO-10 #####
set arrow from 40.000000,-16.158120 to 60.000000, -16.158120 nohead lc 2 linewidth 1.
##### HOMO-9 #####
set arrow from 40.000000,-13.994815 to 60.000000, -13.994815 nohead lc 2 linewidth 1.
##### HOMO-8 #####
set arrow from 40.000000,-12.373017 to 60.000000, -12.373017 nohead lc 2 linewidth 1.
##### HOMO-7 #####
set arrow from 40.000000,-11.836952 to 60.000000, -11.836952 nohead lc 2 linewidth 1.
##### HOMO-6 #####
set arrow from 25.000000,-11.238302 to 45.000000, -11.238302 nohead lc 2 linewidth 1.
##### HOMO-5 #####
set arrow from 55.000000,-11.238302 to 75.000000, -11.238302 nohead lc 2 linewidth 1.
##### HOMO-4 #####
set arrow from 40.000000,-9.700859 to 60.000000, -9.700859 nohead lc 2 linewidth 1.
##### HOMO-3 #####
set arrow from 40.000000,-9.148468 to 60.000000, -9.148468 nohead lc 2 linewidth 1.
##### HOMO-2 #####
set arrow from 40.000000,-9.145747 to 60.000000, -9.145747 nohead lc 2 linewidth 1.
##### HOMO-1 #####
set arrow from 25.000000,-6.625972 to 45.000000, -6.625972 nohead lc 1 linewidth 1.
##### HOMO #####
set arrow from 55.000000,-6.625972 to 75.000000, -6.625972 nohead lc 1 linewidth 1.
##### LUMO #####
set arrow from 25.000000,0.163268 to 45.000000, 0.163268 nohead lc 2 linewidth 1.
##### LUMO+1 #####
set arrow from 55.000000,0.163268 to 75.000000, 0.163268 nohead lc 2 linewidth 1.
##### LUMO+2 #####
set arrow from 40.000000,2.563312 to 60.000000, 2.563312 nohead lc 2 linewidth 1.
##### LUMO+3 #####
set arrow from 25.000000,4.032727 to 45.000000, 4.032727 nohead lc 2 linewidth 1.
##### LUMO+4 #####
set arrow from 55.000000,4.032727 to 75.000000, 4.032727 nohead lc 2 linewidth 1.
##### LUMO+5 #####
set arrow from 40.000000,4.492600 to 60.000000, 4.492600 nohead lc 2 linewidth 1.
##### LUMO+6 #####
set arrow from 40.000000,5.028664 to 60.000000, 5.028664 nohead lc 2 linewidth 1.
##### LUMO+7 #####
set arrow from 40.000000,5.031385 to 60.000000, 5.031385 nohead lc 2 linewidth 1.
##### LUMO+8 #####
set arrow from 40.000000,5.268124 to 60.000000, 5.268124 nohead lc 2 linewidth 1.

plot NaN
