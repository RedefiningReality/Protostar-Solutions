import socket
import struct

HOST = "127.0.0.1"
PORT = 2998

# Establishes connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Receives binary data
data = s.recv(4)

# Converts binary data to unsigned integer
data = struct.unpack("I", data)[0]
# Converts unsigned integer into ASCII string
data = str(data)

# Sends data to server
s.send(data)
# Prints response from server
print s.recv(1024)
