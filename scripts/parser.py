#!/usr/bin/env/python 
f = open("../logs/atm.log")
device = {}
i = 0
TID = []
timeStamp = []
status = []
information = []
for line in f:
		TID.append([line.split("|")[0]])
		timeStamp.append([line.split("|")[1]])
		status.append([line.split("|")[2]])
		information.append([line.split("|")[3]])

print(TID)
print(timeStamp)
print(status)
print(information)
