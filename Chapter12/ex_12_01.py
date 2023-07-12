
import socket

url = input("Enter URL: ")

# used for testing
if len(url) < 1:
    url = "http://data.pr4e.org/romeo.txt"

# split the input between forward-slashes
spl = url.split('/')

# test format
try:
    host = spl[2]

except:
    print("Please enter the URL in proper format:")
    exit()


port = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# checking if URL exists
try:
    mysock.connect((host, port))

except:
    print("Please enter an existing URL:")
    exit()

cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# looping thru 512 characters and printing 
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()