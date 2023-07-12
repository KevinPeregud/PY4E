
# pip install beautifulsoup4
# The program will use urllib to read the HTML from the data files below,
# extract the href= vaues from the anchor tags,
# scan for a tag that is in a particular position relative to the first name in the list,
# follow that link and repeat the process a number of times and report the last name you find.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# requests URL, number of repetition and position of the link
url = input("Enter URL: ")
repeat = int(input("Number of repetitions: "))
pos = int(input("Enter position: "))

# used for testing
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'

# records current names A-Z from URL and store it in a list
sequence = re.findall("_([A-Z].*)[.]", url)

# runs until number of repetition achieved
while True:

    # prints 'Retrieving: ' and current URL
    print(f'Retrieving: {url}')

    if repeat == 0:
        break

    # reads the whole webpage
    html = urlopen(url).read()

    # bs4 to parse html docs
    soup = BeautifulSoup(html, "html.parser")

    # finds all lines containing anchor tags, 
    # up to a limit, and store them in a list
    tags = soup.find_all('a', limit=pos)

    # extracts the name we're looking for and store in str
    name = tags[pos-1].contents[0]

    # appends current name to the sequence list
    sequence.append(name)

    # extracts the URL we're looking for and store in str
    url = tags[pos-1].get('href')

    # subtracts from number a repetions entered
    # count down 
    repeat -= 1

# print outputs
print('\nSequence of names: ', end='')
for name in sequence:
    # prints 'Sequence of names: in a column.
    #print('\nSequence of names: ',name, end=' ')
    # This prints names out in a line
    print(name, end= ' ')
# prints last name in sequence    
print(f'\n\nLast name in sequence: {sequence[-1]}')



