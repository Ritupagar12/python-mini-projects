permissions = 0b1010
read_mask = 0b1000
write_mask = 0b0010

print("Read permission:", bool(permissions & read_mask))
print("Write permission:", bool(permissions & write_mask))
