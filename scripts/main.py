#!/usr/bin/env/python3
f = open("../logs/atm.log")
#print(f.readlines())
for line in f:
	if "ERROR" in line:
		print(line)

