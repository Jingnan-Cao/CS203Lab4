import math

def parser(str, tagL, idxL): 
	slist = str.split(" ") 
	addrHex = slist[-1] # hexidecimal string representation of the address
	if len(addrHex) > 8: # truncate if addrHex is more than 8 characters
		addrHex = addrHex[-8:]
	num = int(addrHex, 16)
	addrBin = bin(num)[2:] # binary string representation of the address
	if len(addrBin) < 32: # padding 0s if addrBin is less than 32 characters
	 	addrBin = (32 - len(addrBin)) * '0' + addrBin
	tag = addrBin[:tagL]
	idx = addrBin[tagL: tagL + idxL]
	return [tag, idx]

def getIdxLen(cache_set_size):
	return int(math.ceil(math.log(cache_set_size, 2)))

#s1 = "L -200 7fffe7ff088"
#s2 = "L 0 d5cb80"

#[x, y] = parser(s2, 20, 10)	
#print getIdxLen(32)