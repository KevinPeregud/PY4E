import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt for URL
url = input('Enter URL: ')

# for testing
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.xml"

# Retrieve the XML data
print('Retrieving', url)
response = urllib.request.urlopen(url)
data = response.read().decode()

# Parse the XML data
print('Retrieved', len(data), 'characters')
try:
    tree = ET.fromstring(data)
except:
    tree = None

# Extract comment counts and compute sum
count_sum = 0
if tree:
    counts = tree.findall('.//count')
    count_sum = sum(int(count.text) for count in counts)
    print('Sum of comment counts:', count_sum)
else:
    print('No comment data found')