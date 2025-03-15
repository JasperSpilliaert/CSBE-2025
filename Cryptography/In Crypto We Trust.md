# CHALLENGE_TITLE
In Crypto We Trust

## Category
Cryptography

## Estimated difficulty
Medium

## Description

We intercepted our enemies' communication of their top-secret flag. However, they use some sort of custom random key that we can't crack! These numbers look so random, our situation seems hopeless.

Given txt file: 
1b60364e0c5b44460758466c0764460107004146016c2105077107066c5808

## Write-up

We know the flag starts with CSC{

XOR‑decrypting the hexadecimal string with a repeating 4‑byte key, we derive the key as:

0x1b ⊕ 'C' (0x43) = 0x58 → X
0x60 ⊕ 'S' (0x53) = 0x33 → 3
0x36 ⊕ 'C' (0x43) = 0x75 → u
0x4e ⊕ '{' (0x7B) = 0x35 → 5

This gives the key "X3u5":

**TODO**

Bytes 0–3: CSC{
Bytes 4–7: Th1s
Byte 8: _
Bytes 9–11: k3Y
Byte 12: _
Bytes 13–15: W34
Byte 16: _
Bytes 17–20: 34sY
Byte 21: _
Bytes 22–23: T0
Byte 24: _
Bytes 25–26: Br
Bytes 27–29: 34k
Byte 30: }

## Solve script

## Flag
`CSC{Th1s_k3Y_W34_34sY_T0_Br34k}`







