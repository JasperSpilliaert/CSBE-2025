# Shout out ChatGPT!!

import base64
from Crypto.Cipher import AES

# Our custom function (same as in the challenge)
def f(x):
    return pow(x, x, 1103)

# Step 1. Read the intercepted numbers from numbers.txt.
with open("numbers.txt") as f_numbers:
    numbers = [int(line.strip()) for line in f_numbers]

# Step 2. Brute-force the PRNG state modulo 1102*1103.
MOD = 1102 * 1103  # = 1,215,506
candidates = []
# We look for the starting state s0 such that:
# for all i in 0...19, f(s0 + i) == numbers[i]
for s in range(1, MOD+1):
    if f(s) == numbers[0]:
        valid = True
        for i in range(1, 20):
            if f(s+i) != numbers[i]:
                valid = False
                break
        if valid:
            candidates.append(s)
            
if not candidates:
    print("No candidate state found!")
    exit()

# We expect a unique candidate.
s0 = candidates[0]
print("Recovered initial state (s0):", s0)

# Step 3. Reconstruct the key.
# The key is formed by the next 32 outputs, each reduced modulo 256.
key_bytes = []
for i in range(20, 20+32):
    key_bytes.append(f(s0+i) % 256)
key = bytes(key_bytes)
print("Recovered AES key (hex):", key.hex())

# Step 4. Decrypt the ciphertext from chal.txt.
with open("chal.txt") as f_chal:
    cipher_b64 = f_chal.read().strip()
ciphertext = base64.b64decode(cipher_b64)

# Create an AES cipher in ECB mode.
cipher = AES.new(key, AES.MODE_ECB)
plaintext = cipher.decrypt(ciphertext)

# Remove the space padding (as used in the challenge).
plaintext = plaintext.rstrip(b' ')
print("Decrypted flag:", plaintext.decode())