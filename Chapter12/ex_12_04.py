# import dependancies
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
import ssl

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# request for URL
url = input('Enter URL: ')

# used for testing
if len(url) < 1:
    url = "http://www.dr-chuck.com/page1.htm"

#  pass URL through BeautifulSoup
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# retrieve all of the paragraph tags and count them
tags = soup('p')
count = 0
for tag in tags:
    count += 1

# print out the total count of paragraph tags found in webpage
print(f"Total count of paragraph tags is {count}")