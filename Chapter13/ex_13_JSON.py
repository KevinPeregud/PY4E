# Extract data fron JSON

from urllib.request import urlopen
import urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Input URL
url = input("Enter URL: ")

# for testing
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.json"

# print 'Receiving' message to match sample
print(f"Retrieving: {url}")

# open URL,read it, and convert it from byte to str
jsn = urlopen(url).read().decode()

# counting total number of characters read
print(f"Retrieving {len(jsn)} characters")

# parse str as json objects
data = json.loads(jsn)

# variables
total = 0
count = 0

# looping through list of 'comments' and count+summing all 'count' values
for comment in data['comments']:
    count += 1
    total += int(comment['count'])

# f output to match sample
print(f"Count: {count}\nSum: {total}")