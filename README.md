plotMO
======
This project is aiming to develop scripts that can help generating MO energy diagram for molecule(s). 

Script List
-----
- plotMO.py:
  - Usage: ```plotMO.py <datafile> [tolerance_for_degeneratio]```
  - Output: Script for gnuplot(it will print out on stdout)
- nodeg/plotMO.py:
  - A new version of plotMO script, no more consider energy degeneracy.
  - Usage: ```plotMO.py <datafile> ```
  - Output: Script for gnuplot(it will print out on stdout)
 
To Do List
-----
 - script to create data file from gaussian log file automatically
 - make the plotMO.py able to ignore useless spaces in data file
 - add some example to the project and document

License
-----
This project is released under terms of <a href="http://en.wikipedia.org/wiki/MIT_License">MIT License </a>

Please feel free to use it in the way you like, as long as you keep the copyright header.
