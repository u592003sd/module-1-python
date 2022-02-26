#flag{pr377y_5u23_7h15_15_n07_w0rd13}

#!/usr/bin/python3
from pwn import *

context.log_level = "critical"

cap=[chr(i) for i in range(65,91)]
sma=[chr(i) for i in range (97, 123)]
dig=[str(i) for i in range (10)]

pc=cap+sma+dig
pc.append("_")
def notwordles(s):
    ex = process('./notwordle')
   
    print(s.encode())
    a = ex.recv()
    ex.sendline(s.encode())
    res = ex.recv()
    res=res.decode()
    print(res)
    ex.close()
    return res


passwd = ""

for i in range(0, 30):
   
    for j in range(len(pc)):      
        response = notwordles(passwd + pc[j])
        correct_characters = []        
        correct_characters = response.rsplit(" ")
        if int(correct_characters[0])==(i+1):          
            passwd+=(pc[j])
            print(passwd)        
            break

print(passwd)
