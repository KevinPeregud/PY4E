# Extract data from XML

from urllib.request import urlopen
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input URL
url = input("Enter URL: ")

# for testing
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.xml"

# print 'Receiving' message to match sample execution
print(f"Retrieving: {url}")

# open URL,read it, and convert it from byte to str
xml = urlopen(url).read().decode()

# counting total number of characters read
print(f"Retrieving {len(xml)} characters")

# converting xml from str to tree
tree = ET.fromstring(xml)

# searching all 'comment' tags and count+summing all contents
sum = 0
count = 0
for comment in tree.findall('comments/comment'):
    count += 1
    sum += int(comment.find('count').text)

# f output to match sample 
print(f"Count: {count}\nSum: {sum}")