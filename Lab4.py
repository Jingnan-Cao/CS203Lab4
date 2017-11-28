#!/usr/bin/env python
import os, sys, math

def parser(str, tagL, idxL): 
    slist = str.split(" ")
    addrHex = slist[-1]
    offset = slist[-2]
    num = long(addrHex, 16) + long(offset)
    addrBin = bin(num)[2:]
    if len(addrBin) < 32:
        addrBin = (32 - len(addrBin)) * '0' + addrBin
    if len(addrBin) > 32:
        addrBin = addrBin[-32:]
    tag = addrBin[:tagL]
    idx = addrBin[tagL: tagL + idxL]
    return [tag, idx]

def getLen(set_size):
    return int(math.ceil(math.log(set_size, 2)))


if len(sys.argv) != 5:
    print "<cache_size  block_size  ways  file_name>"
    sys.exit(0)

#initialize
cache_size = int(sys.argv[1]) * 1024
block_size = int(sys.argv[2])
ways = int(sys.argv[3])
file_name = sys.argv[4]

block_num = cache_size / block_size
if not ways:
	cache_sets = 1
else:
	cache_sets = (block_num - 1) / ways + 1


idxL = getLen(cache_sets)
offsetL = getLen(block_size)
tagL = 32 - idxL - offsetL

visit, miss = 0, 0

CACHE = {}
for i in range(cache_sets):
	iStr = bin(i)[2:]
	if len(iStr) < idxL:
		iStr = (idxL - len(iStr)) * '0' + iStr
	CACHE[iStr] = []

#gcc-10K.memtrace
file = open(file_name, "r+")
line = file.readline()
while line:
    parseLine = parser(line, tagL, idxL)
    tag, idx = parseLine[0], parseLine[1]
    if not ways:
    	idx = '0'
    visit += 1
    hit = False
    for i, addr in enumerate(CACHE[idx]):
    	if addr == tag:
    		hit = True
    		CACHE[idx].pop(i)
    		CACHE[idx].append(tag)
    		break
    if not hit:
    	miss += 1
    	if not ways:
    		if len(CACHE[idx]) == block_num:
    			CACHE[idx].pop(0)
    		CACHE[idx].append(tag)
    	else:
    		if len(CACHE[idx]) == ways:
    			CACHE[idx].pop(0)
    		CACHE[idx].append(tag)  
    line = file.readline()

file.close()

miss_rate = float(miss) / float(visit) * 100.0
print "miss rate: " + str(miss_rate) + "%"
print "hit rate: " + str(100 - miss_rate) + "%"
print "number of sets: " + str(cache_sets)
print "ways: " + str(ways)
print "number of address bits for tag: " + str(tagL)
print "number of address bits for index: " + str(idxL)
print "number of address bits for offset: " + str(offsetL)
print 



