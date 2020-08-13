import bluetooth

bd_addr = "70:BB:E9:2F:A9:93"

port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")

sock.close()