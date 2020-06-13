#First, we should install boom. Run "pip3 install boom" in terminal
#Then we should run the boom command. we'll do it with running "boom hostname -c number_of_clients -n number_of_requests" in terminal
import subprocess
import time

#Asking for inputs
inputnum = input ("How long should I wait until running it for the next time? (Press enter to use default 1 day delay)\n")
if inputnum == "":
    seconds = 86400
else:
    seconds = inputnum

hostname = input ("Hostname? \n")
number_of_clients = input ("Number of clients? \n")
number_of_requests = input ("Number of requests per client? \n")

#Making the command as a string to run later
string = "boom " + hostname + " -c " + number_of_clients + " -n " + number_of_requests

#Loop for scheduling our commands
while True:
    subprocess.run(string)
    print ("Done")
    time.sleep(float(seconds))