fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname)

counts = dict()
largest = 0
k = None

for line in fhand:
    line = line.rstrip()
    if line.startswith ('From:'):
        continue

    elif line.startswith ('From'):
        line = line.split()
        #print(line)
        k = line[1]
        counts[k] = counts.get(k,0)+1
    else:
        continue
        
for k,v in counts.items():
    #print(counts)
    if v > largest :
        largest = v
        email = k
print(email, largest)