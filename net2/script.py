import socket
import struct

HOST = "127.0.0.1"
PORT = 2997

# Establishes connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Receives binary data
data = s.recv(4) + s.recv(4) + s.recv(4) + s.recv(4)

# Converts binary data to set of unsigned integers
data = struct.unpack("IIII", data)
# Sums unsigned integers
data = sum(data)

# Sends data to server
s.send(struct.pack("I", data & 0xffffffff))
# Prints response from server
print s.recv(1024)
