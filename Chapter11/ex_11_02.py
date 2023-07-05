import re

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'regex_sum_1836841.txt'
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()


count = 0
sum = 0

for line in fhand:
    line = line.strip()
    stuff = re.findall('[0-9]+', line)

    if len(stuff)>0:
        for num in stuff:
            #count = count + 1
            #print(count,num)
            #print out the number of values and value
            sum = sum + int(num)

print(sum)