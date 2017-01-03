#!/usr/bin/env python

import subprocess
import sys

#print("")
#print(" The program is going to install and configure the Nagios server automatically.")
#print(" It is supposed that you have already added all IP addresses of client hosts to the 'clients.txt' file.")
#print(" Users must be 'root' with the same passwords on all hosts ...")
#print("")
#print("=====================================================================================")
#print("")
#print(" Firstly we must install/configure Nagios server and secondly clients.")
#print("")

choose = ""

while choose != "3":
    print("Choose one of the following options:")
    print("1. To install Fail2ban and configure for SSH, type 1 and press 'Enter'.")
    print("2. To list and unban blocked IP addresses, type 2 and press 'Enter'.")
    print("3. To exit type 3 and press 'Enter'.")
    print("")
    choose = raw_input("  Please choose the installation option: ")
    if choose == "1":
        subprocess.call("python install.py", shell=True)
        #print("Fail2ban successfully installed and configured!!!")
        print("")
        print("")
    elif choose == "2":
        print("")
        subprocess.call("python listunban.py", shell=True)
        #print("Nrpe and necessary plugins successfully installed and configured on all servers!!!")
        print("")
        print("")
    elif choose == "3":
        sys.exit()
    else:
        print("  You can choose options, only '1','2' or '3' !!!")
