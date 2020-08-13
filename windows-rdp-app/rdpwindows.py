from pypsexec.client import Client
import os
import time
import sys
import paramiko

host = '52.66.21.211'
username = 'Niruban'
password = 'RYz*UKsczxWAp%.GjsU;OFg%N%Vaz$Dt'
output = []

c = Client(host, username=username, password=password, encrypt=False, port=139)
c.connect()

try:
 c.create_service()
 stdout = c.run_executable("cmd.exe", arguments="par")
 output = stdout[0].decode("utf-8")
 print(output.split("\r\n")[1:3])

finally:
 c.cleanup()
 c.remove_service()
 c.disconnect()