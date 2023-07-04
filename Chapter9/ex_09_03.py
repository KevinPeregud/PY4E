fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname)

di = dict()

for line in fhand:
    line = line.rstrip()
    if line.startswith ('From:'):
        continue

    elif line.startswith ('From'):
        line = line.split()
        #print(line)
        k = line[1]
        di[k] = di.get(k,0)+1
    else:
        continue

print(di)