#https://docs.pwntools.com/en/stable/

from pwn import *

print(cyclic(50))
print(cyclic_find("laaa"))
print(shellcraft.sh())

print(hexdump(asm(shellcraft.sh())))

# p = process("/bin/sh")
# p.sendline("echo hello;")
# p.interactive()

r = remote("127.0.0.1", 1234)
r.sendline("hello!")
r.interactive()
r.close()