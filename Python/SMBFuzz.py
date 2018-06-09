import sys,random,struct,socket,lib
from random import *
from lib import *
from socket import *
from boofuzz import *

modded from "http://g-laurent.blogspot.com/2010/05/fuzzing-lib-released.html"


print "Dummy Example"

sess = sessions.Session(session_filename="smb.session", sleep_time=0.10, check_data_received_each_request=False)

target = sessions.Target(SocketConnection("xxx", 445, proto='tcp'))
s_initialize("Lol")

packetnego = [chr(int(a, 16)) for a in """
ff 53 4d 42 72 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 d5 15 00 00 81 0b
00 77 00 02 50 43 20 4e 45 54 57 4f 52 4b 20 50
52 4f 47 52 41 4d 20 31 2e 30 00 02 4d 49 43 52
4f 53 4f 46 54 20 4e 45 54 57 4f 52 4b 53 20 33
2e 30 00 02 44 4f 53 20 4c 4d 31 2e 32 58 30 30
32 00 02 44 4f 53 20 4c 41 4e 4d 41 4e 32 2e 31
00 02 57 69 6e 64 6f 77 73 20 66 6f 72 20 57 6f
72 6b 67 72 6f 75 70 73 20 33 2e 31 61 00 02 4e
54 20 4c 4d 20 30 2e 31 32 00""".split()]
 
packetsession1 = [chr(int(a, 16)) for a in """
ff 53 4d 42 73 00 00 00 00 18 07 00 00 00 00 00
00 00 00 00 00 00 00 00 00 00 ff fe 00 00 04 00
0d 75 00 54 00 68 0b 02 00 00 00 04 06 03 80 01
00 01 00 00 00 00 00 d4 00 00 00 17 00 00 00 57
69 6e 64 6f 77 73 20 37 20 50 72 6f 00 57 49 4e
37 00 00 00 04 ff 00 91 00 08 00 18 00 32 00 00
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
00 00 00 00 00 00 00 5c 5c 31 39 32 2e 31 36 38
2e 31 2e 38 36 5c 49 50 43 24 00 3f 3f 3f 3f 3f
00""".split()]
 
def longueur(payload):
    length = struct.pack(">i", len(''.join(payload)))
    return length
 
def handle(data):
 
    ##Session Setup AndX Request, tree ipc;
    if data[8:10] == "\x72\x00":
       print "Session Query fuzzed sended\n"
       packet0 = ''.join(randfunc(packetsession1)) ### ---> randfunc used ...
       buffer0 = longueur(packet0)+packet0          
       print "complete packet %s\n\n" % (buffer0.encode("hex"))
       return buffer0
    ## no uid/tid/mid/etc care here, this is not a fuzzer release, just an example of using this lib...
    ## put here the Rest of tha RFC/Specs.  
 
##starting prog  
def run():
    host = "xxx",445
    
    sess.add_target(target)
    
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(host)  
    s.settimeout(0.1)
    packet0 = ''.join(randfunc(packetnego)) ### ---> randfunc used ...
    print "Nego fuzzing"
    buffer0 = longueur(packet0)+packet0
    print "complete packet nego %s\n\n" % (buffer0.encode("hex"))
    s.send(buffer0)
    try:
      while True:
        data = s.recv(1024)
        s_string(handle(data))
    except Exception:
        pass
        s.close()
    sess.connect(s_get("Lol"))
    sess.fuzz()
 
while True:
   run()
