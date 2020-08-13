import bluetooth

sock=bluetooth.BluetoothSocket(bluetooth.L2CAP)

bd_addr = "D6:2D:0C:49:2A:4D"
port = 0x1001

sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()