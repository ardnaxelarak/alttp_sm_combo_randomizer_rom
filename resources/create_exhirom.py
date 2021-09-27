#!/usr/bin/env python
import sys
import os
name = ""
base_name = ""

if len(sys.argv) < 4:
	print("create_exhirom.py <super metroid rom> <alttp rom> <output filename> <filler byte>")
	sys.exit()
else:
	sm_name = sys.argv[1]
	alttp_name = sys.argv[2]
	output_name = sys.argv[3]
	filler = int(sys.argv[4] or "0x00", base=16)


f_sm = open(os.path.dirname(os.path.realpath(__file__)) + "/" + sm_name, "rb")
f_alttp = open(os.path.dirname(os.path.realpath(__file__)) + "/" + alttp_name, "rb")
fo = open(os.path.dirname(os.path.realpath(__file__)) + "/" + output_name, "wb")

data = f_sm.read()
for i in range(0, 0x40, 1):	
	hi_bank = data[(i*0x8000):(i*0x8000)+0x8000]
	lo_bank = data[((i+0x40)*0x8000):((i+0x40)*0x8000)+0x8000]
	if len(lo_bank) == 0:
		lo_bank = bytes([filler] * 0x8000)
	if len(hi_bank) == 0:
		hi_bank = bytes([filler] * 0x8000)
		
	fo.write(lo_bank)
	fo.write(hi_bank)

fo.seek(0x400000)

data = f_alttp.read()
for i in range(0, 0x20, 1):	
	hi_bank = data[(i*0x8000):(i*0x8000)+0x8000]
	lo_bank = bytes([filler] * 0x8000)
		
	fo.write(lo_bank)
	fo.write(hi_bank)
	
f_sm.close()
f_alttp.close()
fo.close()
