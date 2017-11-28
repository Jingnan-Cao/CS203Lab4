import math

def parser(str, tagL, idxL): 
    slist = str.split(" ")
    addrHex = slist[-1]
    offset = slist[-2]
    num = long(addrHex, 16) + long(offset)
    print long(addrHex, 16)
    print long(offset)
    print num
    print "%x" % num
    addrBin = bin(num)[2:]

    print addrBin

    if len(addrBin) < 32:
        addrBin = (32 - len(addrBin)) * '0' + addrBin
    if len(addrBin) > 32:
        addrBin = addrBin[-32:]
    tag = addrBin[:tagL]
    idx = addrBin[tagL: tagL + idxL]
    return [tag, idx]

def getIdxLen(cache_set_size):
	return int(math.ceil(math.log(cache_set_size, 2)))

s1 = "L -200 7fffe7ff088"
#s2 = "L 0 d5cb80"

[x, y] = parser(s1, 20, 10)	
print x 
print y
#print getIdxLen(32)