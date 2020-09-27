import socket
import time
import pickle


# CopyRights (c) All Rights Reserved
# Author : Dhanasekara Pandian
# Email : dhana.s@contecuae.com, sekar5in@quehive.com
# Monitoring Agent Application

'''
pickling to serialization of the objects via sockets
'''

# static variables

HEADERSIZE = 10

# Initialize the Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 3001))

while True:
    full_msg = b''
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f'new messag length: {msg[:HEADERSIZE]}')
            msglen = int(msg[:HEADERSIZE])
            new_msg = False   
    
        full_msg += msg

        if len(full_msg) - HEADERSIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADERSIZE:])

            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            
            new_msg = True
            full_msg = b''
    print(full_msg)
