
import urllib.request, urllib.parse, urllib.error

# request URL input
url = input("Enter URL: ")

# used for testing
if len(url) < 1:
    url = "http://data.pr4e.org/romeo-full.txt"

# send GET request and open URL
fhand = urllib.request.urlopen(url)

# variables
total = 0
count = 0
limit = 3000

# loop thru each line of the open URL
for line in fhand:

    # decoding and stripping of unnecessary characters
    line = line.decode().strip()

    # count of total characters
    total += len(line)

    # if count of characters is still less than 3000
    if count < limit:

        #counting
        count += len(line)

        #printing lines 
        if not count > limit:
            print(line)

        # stop displaying characters at 3000
        else:

            ends = (limit - count) + 1 

            # shave the count for accuracy
            count = count - (count - limit)

            # print up to 3000 characters
            print(line[:ends])

print(f"\nCharacter count limit: {count}")
print(f"Total number of characters received: {total}")