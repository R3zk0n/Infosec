import sys
try:length=int(sys.argv[1])
except:print "[+] Usage: %s <length> [set a] [set b] [set c]" % sys.argv[0]; sys.exit(1)

try:seta=sys.argv[2]
except:seta="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
try:setb=sys.argv[3]
except:setb="abcdefghijklmnopqrstuvwxyz"
try:setc=sys.argv[4]
except:setc="0123456789"

string="" ; a=0 ; b=0 ; c=0

while len(string) < length:
    if len(sys.argv) == 2:
        string += seta[a] + setb[b] + setc[c]
        c+=1
        if c == len(setc):c=0;b+=1
        if b == len(setb):b=0;a+=1
        if a == len(seta):a=0
    elif len(sys.argv) == 3:
        print "[!] Error, cannot work with just one set!"
        print "[+] Usage: %s <length> [set a] [set b] [set c]" % sys.argv[0]; sys.exit(1)
        sys.exit(1)
    elif len(sys.argv) == 4:
        string += seta[a] + setb[b]
        b+=1
        if b == len(setb):b=0;a+=1
        if a == len(seta):a=0
    elif len(sys.argv) == 5:
        string += seta[a] + setb[b] + setc[c]
        c+=1
        if c == len(setc):c=0;b+=1
        if b == len(setb):b=0;a+=1
        if a == len(seta):a=0
    else:
        print "[+] Usage: %s <length> [set a] [set b] [set c]" % sys.argv[0]; sys.exit(1)

print "-------------------------------------------------------------------------"
print string[:length]
print "-------------------------------------------------------------------------"
print "Length: %i" % length
print "[+] SetA: '%s'" % seta
print "[+] SetB: '%s'" % setb
if len(sys.argv) != 4: print "[+] SetC: '%s'" % setc
print "-------------------------------------------------------------------------"