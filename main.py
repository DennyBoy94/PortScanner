import socket
import subprocess
import sys
from datetime import datetime

target = "scannme.nmap.org"
targetIP = socket.gethostbyname(target)

tstart = datetime.now()

try:
	for p in range(1, 45000):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		res = sock.connect_ex((targetIP, p))
		if res == 0:
			print("Open connection in Port: " + str(p))
		sock.close()
except Exception:
	print("There was an error.")
	sys.exit()

tend = datetime.now() 
diff = tend - tstart

print("Scan completed in: " + str(diff))