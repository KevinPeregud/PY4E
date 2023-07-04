fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname)

di = dict()

for line in fhand:
    line = line.rstrip()
    if line.startswith ('From:'):
        wds = line.split()
        email = wds[1]
        #print(email)
        ads = email.split('@')
        #print(ads[1])   
        k = ads[1]
        di[k] = di.get(k,0)+1
    else:
        continue

print(di)
    
