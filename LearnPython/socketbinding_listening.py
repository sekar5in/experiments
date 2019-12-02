#!/usr/local/bin/python3

# This socket binding and listening.


import socket
import sys

host = ''
port = 5559

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

s.listen(5)
#onn, addr = s.accept()
#pint('connected' + addr[0] + ':' + str(addr[1]))

