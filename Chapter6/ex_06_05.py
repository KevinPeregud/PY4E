str = 'X-DSPAN-Confidence: 0.8475'
ipos = str.find(':')
#print(ipos)
piece = str[ipos+2:]
#print(piece)
#print(value+42.0)fail
value = float(piece)
print(value)
#print(value+42.0)
