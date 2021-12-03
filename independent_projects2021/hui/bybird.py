#!/usr/bin/env python

import pandas as pd
import numpy as np
import sys
import re

for file in sys.argv[1:]:
	f = pd.read_csv(file)
	f1 = f[0:23]
	for this in f1:
		outfile = "1_" + file
		f1.to_csv(path_or_buf=outfile,index=False,header=False)
	f2 = f[24:47]
	for this in f2:
		outfile = "2_" + file
		f2.to_csv(path_or_buf=outfile,index=False,header=False)
	f3 = f[48:71]
	for this in f3:
		outfile = "3_" + file
		f3.to_csv(path_or_buf=outfile,index=False,header=False)
	f4 = f[72:95]
	for this in f4:
		outfile = "4_" + file
		f4.to_csv(path_or_buf=outfile,index=False,header=False)
	f5 = f[96:119]
	for this in f5:
		outfile = "5_" + file
		f5.to_csv(path_or_buf=outfile,index=False,header=False)
	f6 = f[120:143]
	for this in f6:
		outfile = "6_" + file
		f6.to_csv(path_or_buf=outfile,index=False,header=False)
	f7 = f[144:167]
	for this in f7:
		outfile = "7_" + file
		f7.to_csv(path_or_buf=outfile,index=False,header=False)
	f8 = f[168:191]
	for this in f8:
		outfile = "8_" + file
		f8.to_csv(path_or_buf=outfile,index=False,header=False)
	f9 = f[192:215]
	for this in f9:
		outfile = "9_" + file
		f9.to_csv(path_or_buf=outfile,index=False,header=False)
	f10 = f[216:239]
	for this in f10:
		outfile = "10_" + file
		f10.to_csv(path_or_buf=outfile,index=False,header=False)
	f11 = f[240:263]
	for this in f11:
		outfile = "11_" + file
		f11.to_csv(path_or_buf=outfile,index=False,header=False)
	f12 = f[264:287]
	for this in f12:
		outfile = "12_" + file
		f12.to_csv(path_or_buf=outfile,index=False,header=False)
	f13 = f[288:311]
	for this in f13:
		outfile = "13_" + file
		f13.to_csv(path_or_buf=outfile,index=False,header=False)
	f14 = f[312:335]
	for this in f14:
		outfile = "14_" + file
		f14.to_csv(path_or_buf=outfile,index=False,header=False)
	f15 = f[336:359]
	for this in f15:
		outfile = "15_" + file
		f15.to_csv(path_or_buf=outfile,index=False,header=False)
	f16 = f[360:383]
	for this in f16:
		outfile = "16_" + file
		f16.to_csv(path_or_buf=outfile,index=False,header=False)
	f17 = f[384:407]
	for this in f17:
		outfile = "17_" + file
		f17.to_csv(path_or_buf=outfile,index=False,header=False)
	f18 = f[408:431]
	for this in f18:
		outfile = "18_" + file
		f18.to_csv(path_or_buf=outfile,index=False,header=False)
	f19 = f[432:455]
	for this in f19:
		outfile = "19_" + file
		f19.to_csv(path_or_buf=outfile,index=False,header=False)
	f20 = f[456:479]
	for this in f20:
		outfile = "20_" + file
		f20.to_csv(path_or_buf=outfile,index=False,header=False)
	f21 = f[480:503]
	for this in f21:
		outfile = "21_" + file
		f21.to_csv(path_or_buf=outfile,index=False,header=False)
	f22 = f[504:527]
	for this in f22:
		outfile = "22_" + file
		f22.to_csv(path_or_buf=outfile,index=False,header=False)
	f23 = f[528:551]
	for this in f23:
		outfile = "23_" + file
		f23.to_csv(path_or_buf=outfile,index=False,header=False)
	f24 = f[552:575]
	for this in f24:
		outfile = "24_" + file
		f24.to_csv(path_or_buf=outfile,index=False,header=False)
	f25 = f[576:599]
	for this in f25:
		outfile = "25_" + file
		f25.to_csv(path_or_buf=outfile,index=False,header=False)