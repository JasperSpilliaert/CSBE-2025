# CHALLENGE_TITLE
Two-time pad

## Category
Cryptography

## Estimated difficulty
Easy

## Description

A one-time pad offers perfect security, but needs tons of keys.

I improved it to only need half as many keys! I'm gonna be a millionaire!

chal.py:

``` py
import os

with open('flag.txt') as file:
    m1 = file.read().strip().encode()
m2 = b'I can\'t believe that no one has thought of this scheme yet'

k = os.urandom(len(m1))

def xor(bytes1, bytes2):
    return bytes(a1 ^ a2 for a1, a2 in zip(bytes1, bytes2))

c1 = xor(m1, k)
c2 = xor(m2, k[1:] + k[:1])

with open('chal.txt', 'w') as file:
    file.write(f'{int.from_bytes(c1, "big")}\n')
    file.write(f'{int.from_bytes(c2, "big")}\n')
```

chal.txt:

36090144755922289111874149912624586104827141550480778361069701468216394000169793076847790901596641569849475155408120250872696688660895686540
44650713323251381086823566213137067535302450177582800043899613361403721543722305609301335578791112968915202037730763136493855017631800923382

## Write-up

now use the following [script](./Resources/ChatGPT.py) to decode 

## Solve script
`Resources/ChatGPT.py`

## Flag
`CSC{p@d_M3_0nc3_sh5m3_oN_y0U_p@d_mE_7w1c3_thats_just_dumb}`


