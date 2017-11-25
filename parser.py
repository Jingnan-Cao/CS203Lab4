
def parser(str, tagL, idxL): 
	slist = str.split(" ")
	addrHex = slist[-1]
	if len(addrHex) > 8:
		addrHex = addrHex[-8:]
	num = int(addrHex, 16)
	addrBin = bin(num)[2:]
	if len(addrBin) < 32:
	 	addrBin = (32 - len(addrBin)) * '0' + addrBin
	tag = addrBin[:tagL]
	idx = addrBin[tagL: tagL + idxL]
	return [tag, idx]

s1 = "L -200 7fffe7ff088"
s2 = "L 0 d5cb80"

[x, y] = parser(s2, 20, 10)	