#!/usr/bin/python2.7

#script to change range numbers like 1-4 5-20 to a serior of number.

import sys



def main():
	nums = ""
	for argv in sys.argv[1:]:
		if len(argv.split("-")) < 2:
			nums = nums + (" %d " % int(argv))
		else:
			(start,end) = argv.split("-")
			start = min(int(start),int(end))
			end = max(int(start),int(end))
			for i in range(start,end+1):
				nums = nums + (" %d " % i)
	print nums


if __name__=='__main__':
	main()
	exit(0)