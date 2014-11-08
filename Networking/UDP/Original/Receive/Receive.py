# Echo server program - receiving
print("Echo server program - receiving")

import socket

HOST = '127.0.0.1'                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)

while 1:
    data = conn.recv(1024)
    if data:
        print("Received data: " + data.decode("utf-8"))
    
    conn.send(data)
conn.close()

input()
