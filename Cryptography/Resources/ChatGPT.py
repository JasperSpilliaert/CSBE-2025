c1_int = 36090144755922289111874149912624586104827141550480778361069701468216394000169793076847790901596641569849475155408120250872696688660895686540
c2_int = 44650713323251381086823566213137067535302450177582800043899613361403721543722305609301335578791112968915202037730763136493855017631800923382

# Known plaintext m2
m2 = b"I can't believe that no one has thought of this scheme yet"

# Assume key length equals length of m2 (the zip in xor stops at the shorter sequence)
n = len(m2)

# Convert integers to bytes (big-endian with padding to n bytes)
c1 = c1_int.to_bytes(n, 'big')
c2 = c2_int.to_bytes(n, 'big')

# Compute the rotated key: for each index, k[(i+1) mod n] = c2[i] XOR m2[i]
k_rot = bytes(a ^ b for a, b in zip(c2, m2))

# Recover the original key by rotating right by one position:
# k_rot = k[1:] + k[:1]  =>  k = k_rot[-1:] + k_rot[:-1]
k = k_rot[-1:] + k_rot[:-1]

# Now decrypt m1: m1 = c1 XOR k
m1 = bytes(a ^ b for a, b in zip(c1, k))
print(m1)
