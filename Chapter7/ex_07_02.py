fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File not found:', fname)
    exit()
    
count = 0
tot = 0

for line in fhand:    

    if 'X-DSPAM-Confidence:' in line:

        count = (count + 1)

        var = line.find(' ')

        tot = float(line[var:]) + tot

print('Average spam confidence:', tot/count)





