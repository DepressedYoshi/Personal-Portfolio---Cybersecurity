#!/bin/python3

import sys ## allows us to enter command line argumetn among other things 
import socket
from datetime import datetime
#this is def stollen from internet, code foundation someone sle, DO NOT USE 

#define our target 
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate a host anme tp IPV4
else:
    print("Invalid amount of arguments")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

#PRetty banner 
print("-" * 50)
print("scanning target " + target)
print("time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range (50,85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) # this is a float
        result = s.connect_ex((target,port))
        print("Checking port {}".format(port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\nExiting Programe.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("could not connect to server")
    sys.exit()


