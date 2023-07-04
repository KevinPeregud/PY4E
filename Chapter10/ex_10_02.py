fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'mbox-short.txt'
fhand = open(fname)

counts = dict()
for line in fhand:
    line = line.rstrip()
    if line.startswith ('From:'):
        continue

    elif line.startswith ('From'):
        line = line.split()
        #print(line)
        time = line[5]
        #print(time)
        hrs = time.split(':')       
        #print(hrs[0])
        hr = hrs[0]
        counts[hr] = counts.get(hr,0)+1

for k,v in sorted(counts.items()):
    print(k,v)



