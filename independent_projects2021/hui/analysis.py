#!/usr/bin/env python


import sys
import re


for file in sys.argv[1:]:
	IN = open(file, 'r')
	match = re.search("(\w+) (\d+), (\d+)", file)
	date = [match.group(1), match.group(2), match.group(3)]
	OUT=open("out_" + file, 'w')
	for Line in IN:
		if re.search("^\d+ ", Line):
			Line = Line.strip("\n")
			a=[]
			for word in Line.split():
				if word.isdigit():
					a.append(int(word))
			OUT.write("%d" % sum(a))
			OUT.write("\n")
		else:
			OUT.write("\n")
	IN.close()
	OUT.close()

