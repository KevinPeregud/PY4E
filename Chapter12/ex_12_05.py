# socket from ex_12_01.py
# Change the socket program so that it only shows data after the headers
# and a blank line have been received.
# Remember that recv receives characters (newlines and all), not lines.
import socket

url = input("Enter URL: ")
port = 80

# used for testing
if len(url) < 1:
    url = 'http://data.pr4e.org/romeo.txt'

spl = url.split('/')

try:
    host = spl[2]

except:
    print("Please enter the URL in proper format!")
    exit()

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((host, port))

except:
    print("Please enter an existing URL!")
    exit()

cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# 'content' to hold the web page's content
content = ''
while True:
    data = mysock.recv(512)

    if len(data) < 1:
        break

    # data is appended to content, 512 bytes at a time
    content += data.decode()

# locating the blank line after the header info
pos = content.find('\r\n\r\n')

# print content after skipping the position of the end line characters
print(content[pos+4:])