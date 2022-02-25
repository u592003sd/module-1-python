# flag{b1n42y_s3r2ch_f7w}

from pwn import *

def bruteforcer(s):
    exe = process('./bruteforcer')
    context.log_level = "critical"

    exe.recv()
    exe.sendline(s)
    response = exe.recvuntil("\n", drop=1).decode("latin-1")
    
    exe.close()
    return response


words =[]
f = open('wordlist.txt', 'r+')
for line in f.readlines():
    words.append(line)
    
f.close()

words.sort()

maximum = len(words)
minimum = 0

while 1:
    index = (minimum + maximum)//2
    res = bruteforcer(words[index])

    if (res == "WRONG :( Key too low"):
        minimum = index

    elif (res == "WRONG :( Key too high"):
        maximum = index

    else:
        print(words[index])
        print(res)
        break

'''
OUTPUT
[+] Starting local process './bruteforcer': pid 2902
bruteforcer.py:8: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  exe.sendline(s)
bruteforcer.py:9: BytesWarning: Text is not bytes; assuming ASCII, no guarantees. See https://docs.pwntools.com/#bytes
  response = exe.recvuntil("\n", drop=1).decode("latin-1")
pennilessa
'''

#enter penniless in the program manually to get the flag
