#!/usr/bin/env python
import sys
import os

if sys.argv[1] == "":
	print("create_dummies.py <00_file> <ff_file> <size_in_mb>")
	sys.exit()
else:
	zero_name = sys.argv[1]
	ff_name = sys.argv[2]
	size = int(sys.argv[3] or "6")

fo_z = open(os.path.dirname(os.path.realpath(__file__)) + "/" + zero_name, "wb")
fo_f = open(os.path.dirname(os.path.realpath(__file__)) + "/" + ff_name, "wb")

fo_z.write(bytes([0x00] * 1024 * 1024 * size))
fo_f.write(bytes([0xff] * 1024 * 1024 * size))

fo_z.close()
fo_f.close()
