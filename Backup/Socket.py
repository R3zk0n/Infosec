#Basic Python Socket implementation, Banner Grabbing
# Thus we sit as one man, confused lost and stressed, no job and no money but with alot of talent and a gift for being able to adapt to all things..


# Added Updated Port Range..
import socket
import sys
import subprocess
import select
#Clearing Screen.
subprocess.call('clear', shell=True)

print "Basic Python Sockets"

User_input = raw_input("Select.. 1 . Selective Scanner || 2 . Range Scanner \n")

# Add Selective ports and port range scanner.
if User_input == '1':
	IP = raw_input("Please enter a IP Address: \n")
	port = input("Please Enter a port num to scan :\n")
	socket.setdefaulttimeout(1)
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect_ex((IP,port))
		s.send("Hello")
		ans = s.recv(4096)
		print IP
		print "[+] The IP "+str(IP)+" On Port: "+str(ans)

	except socket.error:
		print "NO ACCESS."
		sys.exit()


if User_input == '2':
	Ip2 = raw_input("Please enter a ip address to scan \n")
	socket.setdefaulttimeout(1)
	try:
		for port in range(1,1025):
			sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			connection = sck.connect_ex((Ip2, port))
			sck.send("Hello")
			ans = sck.recv(1024)
			print Ip2
			print "[=]The IP "+str(Ip2)+"On PORT:"+str(ans)
	except socket.error:
		print "No Connection"
		sys.exit()
