# Echo server program - receiving

import threading

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

'''while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message:" + data.decode("utf-8"))


'''

clientList = []


# Message received
def receiving():

    data, addr = sock.recvfrom(1024)
    
    if data:
        print("Received data: " + data.decode("utf-8"))

        print(addr)

        if not addr in clientList:

            clientList.append(addr)
    recThread.start()

# Message sender
def sending(data, bing):

    for i in range(0, len(clientList)):
        clientList[i].send(data)

# Message receive thread
recThread = threading.Thread(target=receiving)

recThread.start()

# Message send thread
sendThread = threading.Thread(target=sending)


'''while 1:
  
    data, addr = sock.recvfrom(1024)
    
    if data:
        print("Received data: " + data.decode("utf-8"))

        print(addr)

        if not addr in clientList:

            clientList.append(addr)

        
conn.close()

input()
'''
