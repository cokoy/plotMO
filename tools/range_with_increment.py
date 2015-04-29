#!/usr/bin/python2.7

#script to print ranges of number with increment

import sys



def main():
	nums = ""
	total = 0
	for argv in sys.argv[1:]:
		for singlerange in argv.split(","):
			seperate_range = singlerange.split(":")
			if len(seperate_range) < 2:
				nums = nums + ("%d, " % int(singlerange))
				total += 1
				if total % 7 == 0:
					nums = nums[:-2] + "\\\n"
			elif len(seperate_range) == 2:
				(start,end) = seperate_range
				start = min(int(start),int(end))
				end = max(int(start),int(end))
				for i in range(start,end+1):
					nums = nums + ("%d, " % i)
					total += 1
					if total % 7 == 0:
						nums = nums[:-2] + "\\\n"
			else:
				(start,end,incr) = seperate_range
				start= min(int(start),int(end))
				end = max(int(start),int(end))
				incr = int(incr)
				#print start, end, incr
				for i in range(start,end+1,incr):
					nums = nums + ("%d, " % i)
					total += 1
					if total % 7 == 0:
						nums = nums[:-2] + "\\\n"
	print total
	print nums


if __name__=='__main__':
	main()
	exit(0)