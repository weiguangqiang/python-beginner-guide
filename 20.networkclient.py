# !/usr/bin/Python

# website: http://pythonprogramminglanguage.com/python-socket-client-network/

import socket
import sys

'''
The steps:
1. creat socket
2. get server ip address from domain name
3. connect to server using ip address
4. send request to server
5. receive data (webpage)
'''

host = 'www.pythonprogramminglanguage.com'
port = 80

# create socket
print("# Creating Socket")
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

print("# Getting remote IP")
try:
    remote_ip = socket.gethostbyname(host)
except socket.gaierror:
    print("Hostname could not be resolved. Exiting")
    sys.exit()

print("# Connecting to server, " + host + " (" + remote_ip + ")")
s.connect((remote_ip, port))

# send data to remote server
print("# Sending data to server")
request = "GET / HTTP/1.0\r\n\r\n"

try:
    # param 'request' must be encoded
    s.sendall(request.encode('utf-8'))
except socket.error:
    print('Send Failed')
    sys.exit()

# receive data
print("# Receive data from server")
reply = s.recv(1024)

print(reply)
