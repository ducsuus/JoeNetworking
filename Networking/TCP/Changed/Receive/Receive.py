# Echo server program - receiving
print("Echo server program - receiving")

import socket
import threading
import time

HOST = '127.0.0.1'                 # Symbolic name meaning the local host
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('Connected by ' + str(addr))

clientList = [conn]

conn.send("meep".encode("utf-8"))

# Connection handeling
def connecting():

    s.listen(1)
    conn, addr = s.accept()

    clientList.append(conn)

# Message received
def receiving():

    '''data = conn.recv(1024)

    print("RECEIVED DATA!")

    if data:

        # Message send thread
        sendThread = threading.Thread(target=sending, args=(data, 2))
        sendThread.start()'''

# Message sender
def sending(data, bing):

    for i in range(0, len(clientList)):
        clientList[i].send(data)

# Connection thread
conThread = threading.Thread(target=connecting)

conThread.start()

# Message receive thread
recThread = threading.Thread(target=receiving)

recThread.start()

# Message send thread
sendThread = threading.Thread(target=sending)


'''while 1:
  
    data = conn.recv(1024)
    if data:
        print("Received data: " + data.decode("utf-8"))

        s.send(data)'''

        
conn.close()

input()
