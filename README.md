plotMO
======
This project is aiming to develop scripts that can help generating MO energy diagram for molecule(s). 

Script List
-----
- plotMO_deg.py:

The original script I create to plot the MO diagram. However, It looks not very good.
  - Usage: ```plotMO.py <datafile> [tolerance_for_degeneratio]```
  - Output: Script for gnuplot(it will print out on stdout)


- plotMO.py:

A new version of plotMO script, no more consider energy degeneracy.
  - Usage: ```plotMO.py <datafile> ```
  - Output: Script for gnuplot(it will print out on stdout)

-  glog2MOinfo.py:
Get MO energy information from Gaussian log file.
  - Usage: ``` glog2MOinfo.py <gaussian log> ```
  - Output: Data file contain all MO energies and type(occ, HOMO, virt)
To Do List
-----
 - <del>script to get MO data file from gaussian log file automatically</del>
 - <del>make the plotMO.py able to ignore useless spaces in data file</del>
 - <del>add some example to the project and document</del>
 - improve the script
 - prepare color for plotMO.py input file

License
-----
This project is released under terms of <a href="http://en.wikipedia.org/wiki/MIT_License">MIT License </a>

Please feel free to use it in the way you like, as long as you keep the copyright header.
