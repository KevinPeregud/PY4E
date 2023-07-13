import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt for URL
url = input('Enter URL: ')

# for testing
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.json"

# Retrieve the JSON data
print('Retrieving', url)
response = urllib.request.urlopen(url)
data = response.read().decode()

# Parse the JSON data
print('Retrieved', len(data), 'characters')
try:
    json_data = json.loads(data)
except:
    json_data = None

# Extract comment counts and compute sum
if json_data and 'comments' in json_data:
    comments = json_data['comments']
    count_sum = sum(comment['count'] for comment in comments)
    print('Sum of comment counts:', count_sum)
else:
    print('No comment data found')