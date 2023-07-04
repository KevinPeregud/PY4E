fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)
di = dict()
for line in hand:
    line = line.rstrip()
    #print (line)
    wds = line.split()
    #print(wds)
    for w in wds:
        if w in di:
           # Idiom: retrieve/create/update count
           di[w] = di.get(w,0) + 1
        else:
            di[w] = 1
         
#print(di)

tmp = list()
for k,v in di.items():
    #print(k,v)
    newtup = (v,k)
    tmp.append(newtup)

#print(tmp)
tmp = sorted(tmp, reverse=True)
#print('Sorted', tmp[:5])
for v,k in tmp[:5] :
    print(k,v)

    
