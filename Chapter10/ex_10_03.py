import string
# must import string or line 11 error
fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'
fhand = open(fname)

di = dict()

for line in fhand:
    # deleting everything but lowercase letters
    line = line.translate(str.maketrans('', '', string.punctuation+'0123456789 \t\n\r')).lower()

    # read through each letter and store in dictionary
    for letter in line:
        di[letter] = di.get(letter, 0) + 1
        #print(di)
lst = list()
for key,val in di.items():
    newtup = (val,key)
    lst.append(newtup)
lst = sorted(lst,reverse=True)
for val,key in lst:
    print(key,val)

