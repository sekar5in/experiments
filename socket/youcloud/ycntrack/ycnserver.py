import socket
import time
import pickle

# CopyRights (c) All Rights Reserved
# Author : Dhanasekara Pandian
# Email : dhana.s@contecuae.com, sekar5in@quehive.com
# Monitoring Server Application

# static variables
HEADERSIZE = 10

# Initialize the Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3001))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")
    
    d = {1: "hey", 2: 'There'}
    msg = pickle.dumps(d)  

    msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg
    clientsocket.send(msg)