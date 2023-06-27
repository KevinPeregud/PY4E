fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    # Guardian a bit strong <3 from <1 before
    # So the line needs at least 3 words
    #if len(words) < 3:
        #continue
    # Or the Guardian in a compound statement
    # **Note** the Guardian has to come first
    if len(words) <3 or words[0] != 'From' : 
        continue
    print(words[2])