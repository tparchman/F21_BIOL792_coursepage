#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys
import re

OUT = open(sys.argv[1], 'w') #Second entry needs to be name of OUT file

for file in sys.argv[2:]:
	IN = open(file, 'r')
	match = re.search("(\d+)_out_(\w+) (\d+), (\d+)", file)
	date = [match.group(2), match.group(3), match.group(4)]
	bird = [match.group(1)]
	for Line in IN:
		Line=Line.strip("\n")
		OUT.write(Line + "\n")
	IN.close()


OUT.close() 