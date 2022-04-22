from pwn import *

KEY_LEN = 50000
MAX_CHUNK = 1000

r = remote("mercury.picoctf.net", 64260)
r.recvuntil(b"This is the encrypted flag!\n")
flag = r.recvlineS(keepends = False)
log.info(f"Flag: {flag}")
bin_flag = unhex(flag)

counter = KEY_LEN - len(bin_flag)

with log.progress('Causing wrap-around') as p:
    while counter > 0:
        p.status(f"{counter} bytes left")
        chunk_size = min(MAX_CHUNK, counter)
        r.sendlineafter(b"What data would you like to encrypt? ", b"a" * chunk_size)
        
        counter -= chunk_size

r.sendlineafter(b"What data would you like to encrypt? ", bin_flag)
r.recvlineS()
flag = unhex(r.recvlineS())
log.success("The flag: picoCTF{" + flag.decode() + "}" )
