#!/usr/bin/env python
import socket
import subprocess
import sys

# Clear the screen
subprocess.call('clear', shell=True)

# Get a host as an input for scanning
remoteServer    = input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Banner
print ("-" * 60)
print ("Please wait, scanning remote host", remoteServerIP)
print ("-" * 60)

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)
# We also put in some error handling for catching errors

try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print ("Port {}: 	 Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print ("Keyboard interrupt, Exiting...")
    sys.exit()

except socket.gaierror:
    print ('Hostname could not be resolved. Exiting...')
    sys.exit()

except socket.error:
    print ("Couldn't connect to server.")
    sys.exit()