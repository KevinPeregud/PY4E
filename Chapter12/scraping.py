from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# request URL
url = input('Enter URL: ')

# used for testing
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.html'

html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

count = 0
total = 0

# adjust tag then search and store
tags = soup('span')

# looping through each span tag and extract the content
for tag in tags:
    total += int(tag.contents[0])
    count += 1
    
#print f output
print(f'Count {count}\nSum {total}')