fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)
di = dict()
for line in hand:
    line = line.rstrip()
    #print (line)
    wds = line.split()
    print(wds)
    for w in wds:
        # If not there the count is zero
        oldcount = di.get(w,0)
        print(w,'old',oldcount)

        newcount = oldcount + 1
        di[w] = newcount
        print(w,'New',newcount)

        #if w in di:
         #   di[w] = di [w] + 1
        #else:
         #   di[w] = 1
            
print(di)