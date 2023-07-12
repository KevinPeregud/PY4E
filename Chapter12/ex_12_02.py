
import socket

url = input("Enter URL: ")

if len(url) < 1:
    url = "http://data.pr4e.org/romeo-full.txt"

spl = url.split('/')

try:
    hostname = spl[2]

except:
    print("Please enter the URL in proper format:")
    exit()

port = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((hostname, port))

except:
    print("Please enter an existing URL:")
    exit()

cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

# new variables for this assignemnt
count = 0
total = 0
limit = 3000

while True:
    data = mysock.recv(500)
    # count total number of characters passing through the socket
    total += len(data)

    if len(data) < 1:
        break

    # store count
    elif total >= limit+1:
        count = limit
        continue

    print(data.decode(), end='')

# print
print(f"\n\nCharacter count limit: {count}")
print(f"Total number of characters: {total}")

mysock.close()