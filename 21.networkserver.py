# !/usr/bin/Python

# website: http://pythonprogramminglanguage.com/socket-server-network

'''
A server can be created using sockets.
Sockets work on the application layer,
it does not specify any protocol and on this level
you’d define an application protocol yourself.
'''

import socket
import sys

'''
The steps:
1. bind socket to port
2. start listening
3. wait for client
4. receive data
'''

HOST = ''
PORT = 8000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("# Socket created")

# Create sockt on port
try:
    s.bind((HOST, PORT))
except s.error as msg:
    print("# Bind Failed")
    sys.exit()

print("# Socket bind complete")

# Start listening on socket
s.listen(10)
print("# Socket now listening")

# Wait for client
conn, addr = s.accept()
print("# Connected to " + addr[0] + ":" + str(addr[1]))

# Receive data from client
while True:
    data = conn.recv(1024)
    line = data.decode("utf-8") # convert to string (Python 3 only)
    line = line.replace("\n", "") # remove newline character
    print(line)

s.close()
