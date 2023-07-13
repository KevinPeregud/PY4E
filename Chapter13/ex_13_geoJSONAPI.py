import urllib.parse
import urllib.request
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt for location
location = input('Enter location: ')

# Construct the API URL
base_url = 'http://py4e-data.dr-chuck.net/json?'
params = {'address': location, 'key': 42}
url = base_url + urllib.parse.urlencode(params)

# Make the API request and retrieve the JSON response
print('Retrieving', url)
response = urllib.request.urlopen(url)
data = response.read().decode()

# Parse the JSON response
print('Retrieved:', len(data), 'characters')
try:
    json_data = json.loads(data)
except:
    json_data = None

# Extract the place_id
if json_data and 'results' in json_data:
    place_id = json_data['results'][0]['place_id']
    print('Place ID: ', place_id)
else:
    print('No place ID found')