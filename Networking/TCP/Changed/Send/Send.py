# Echo client program - sending
print("Echo client program - sending")

import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007          # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


##s.send('Hello, world!'.encode('utf8'))
while True:
    s.send(input().encode('utf8'))
    data = s.recv(1024)
    
    print('Received', repr(data))

s.close()

input()
