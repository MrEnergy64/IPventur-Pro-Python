#!/usr/bin/env python3
# -*- coding: utf8 -*-
# Author: Mr. Energy
# Version 2.0 - 28. August 2020

import os
import time
import pathlib
import ipaddress
import cmd
import datetime

from time import gmtime, strftime
from pathlib import Path
from datetime import date
from datetime import datetime


# os.system('cls')  # For Windows
os.system('clear')  # For Linux/OS X



banner = ("""

     \033[1;m
    ___   ___________                                          ___                             
    |\033[1;94m░░\033[1;m|  |\033[1;94m░░░░░░░░░\033[1;m \                                         |░░|                              
    |\033[1;94m░░\033[1;m|  |\033[1;94m░░░░\033[1;mIP\033[1;94m░░░░\033[1;m \                                        |░░|                              
    |\033[1;94m░░\033[1;m|  |\033[1;94m░░░░\033[1;mIPIP\033[1;94m░░░\033[1;m \                                       |░░|                              
    |\033[1;94m░░\033[1;m|  |\033[1;94m░░░░\033[1;mIPIPI\033[1;94m░░░\033[1;m|                                       |░░|                              
    |\033[1;94m░░\033[1;m|  |\033[1;94m░░░░\033[1;mIPI\033[1;94m░░░░\033[1;m /       Author:  Mr. Energy             |░░|                              
    |\033[1;94m░░\033[1;m|  |\033[1;94m░░░░░░░░░░\033[1;m /        Version: 2.0 Pro                |░░|                              
    |\033[1;94m░░\033[1;m|  |\033[1;94m░░\033[1;m|-------- __        __    ________   __  ____   __|░░|__   ___    __   __           
    |\033[1;94m░░\033[1;m|  |\033[1;94m░░\033[1;m|         |░|       |░|  /░░░░░░░░\  |░|/░░░░\ |░░░░░░░░|  |░|    |░|  |░|  __      
    |\033[1;94m░░\033[1;m|  |\033[1;94m░░\033[1;m|          |░|     |░|   |░░IPIP░░|  |░/░/  \░\   |░░|     |░|    |░|  |░|/░░░\\     
    |\033[1;94m░░\033[1;m|  |\033[1;94m░░\033[1;m|           |░|   |░|    |░░░░░░░/   |░░/   |░|   |░░|     |░|    |░|  |░/░/ \░\\    
    |\033[1;94m░░\033[1;m|  |\033[1;94m░░\033[1;m|  ░░░░░░    |░| |░|     |░/    __   |░/    |░|   |░░|     |░|    |░|  |░░/         
    |\033[1;94m░░\033[1;m|  |\033[1;94m░░\033[1;m|             |░ ░|      |░|    |░|  |░|    |░|   |░░|     |░|    |░|  |░|          
    |\033[1;94m░░\033[1;m|  |\033[1;94m░░\033[1;m|              |░|       \░\____/░|  |░|    |░|   \░░\__   \░\____/░/  |░|          
    ----  ----               |         \░░░░░░░/  |░|    |░|    \░░░░|   \░░░░░░/   |░|          \033[1;m
   
      

    \033[1;94mIP-Ventur Pro 2.0\033[1;m IP collection with nmap

    Github: https://github.com/MrEnergy64

    \033[1;33mLet's collect IP details, before we pentest it!\033[0m
    """)

print(banner)
time.sleep(0.4)

# check if fping and nmap installed
which = None
which = lambda y: next(filter(lambda x: os.path.isfile(x) and os.access(x,os.X_OK),[x+os.path.sep+y for x in os.getenv("PATH").split(os.pathsep)]),None)

check1 = ()
check2 = ()

check1 = which("fping")

print("\n    -> Checking for existing program files \"\033[1;94mnmap\033[1;m\" and \"\033[1;94mfping\033[1;m\"  .......")
time.sleep(1.0)

if check1 == (None):
    print("\n    :-( Sorry, but I require \"\033[1;94mfping\033[1;m\", but it's not installed!  Please install it. Check Out: \033[1;94mhttps://github.com/schweikert/fping\033[1;m")
    time.sleep(1.0)
    exit()
else:
    print("\n    [OK] Program \"\033[1;94mfping\033[1;m\" is installed!"
    )
    time.sleep(1.0)

check2 = which("nmap")

if check2 == (None):
    print("\n    :-( Sorry, I require \"\033[1;94mnmap\033[1;m\", but it's not installed!  Please install it. Check Out: \033[1;94mhttps://github.com/nmap/nmap\033[1;m")
    time.sleep(1.0)
    exit()
else:
    print("\n    [OK] Program \"\033[1;94mnmap\033[1;m\" is installed!")
    time.sleep(1.0)

print("\n\n    -> Checking if the  \"\033[1;94mnmap\033[1;m\" Script-Folder exist .......")
time.sleep(1.0)

dir1 = ()
dir2 = ()
nmap_script = None
my_dir = None

my_dir = Path("~/.nmap/scripts")
if my_dir.is_dir():
    print ("\n    [OK] Folder \"\033[1;94m~/.nmap/scripts\033[1;m\" exist")
    time.sleep(1.0)
    dir1 = 1
else:
    print ("\n    [none] Folder \"\033[1;94m~/.nmap/scripts\033[1;m\" does not exist!")
    dir1 = 0
    time.sleep(1.0)

my_dir = Path("/usr/share/nmap/scripts")
if my_dir.is_dir():
    print ("\n    [OK] Folder \"\033[1;94m/usr/share/nmap/scripts\033[1;m\" exist")
    dir2 = 1
    time.sleep(1.0)
else:
    print ("\n    [none] Folder \"\033[1;94m/usr/share/nmap/scripts\033[1;m\" does not exist!")
    dir2 = 0
    time.sleep(1.0)

if dir1 == 1 and dir2 == 0:
    print("\n    -=> \033[1;94mNOTE:\033[1;m Use NMAP-Script Folder: \"\033[1;94m~/.nmap/scripts\033[1;m\" ")
    time.sleep(2.0)
    nmap_script_pfad = '~/.nmap/scripts/'
elif dir1 == 0 and dir2 == 1:
    print("\n    -=> \033[1;94mNOTE:\033[1;m Use NMAP-Script Folder: \"\033[1;94m/usr/share/nmap/scripts\033[1;m\" ")
    time.sleep(2.0)
    nmap_script_pfad = '/usr/share/nmap/scripts/'
elif dir1 == 1 and dir2 == 1:
    print("\n    -=> \033[1;94mNOTE:\033[1;m Use NMAP-Script Folder: \"\033[1;94m/usr/share/nmap/scripts\033[1;m\" ")
    time.sleep(2.0)
    nmap_script_pfad = '/usr/share/nmap/scripts/'
elif dir1 == 0 and dir2 == 0:
    print("\n    !!! No standard NMAP Script folder exist !!! Therefore you cannot the NMAP Script scanning option! ")
    time.sleep(2.0)


while True:

    # os system('cls') # For Windows OS
    os.system('clear')  # For Linux/OS X
    print(banner)

    IP_version = ()

    print('\n    -> Which IP Version you would like to use: ')
    IP_version = input('       \033[1;94mIPv4 (1)\033[1;m or \033[1;94mIPv6 (2)\033[1;m ? [Press \033[1;94m1\033[1;m or \033[1;94m2\033[1;m, then ENTER] ')

    if IP_version == "1":
        print("\n    -> You would like \033[1;94mIPv4\033[1;m scan.")
        time.sleep(2.0)
        break

    elif IP_version == ("2"):
        print("\n    -> You would like \033[1;94mIPv6\033[1;m scan.")
        time.sleep(2.0)
        break

    else:
        print("\n    -> Your input is wrong! Please just use \033[1;94m1\033[1;m or \033[1;94m2\033[1;m as input.")
        time.sleep(2.0)
        continue

Ip = ()

if IP_version == ("2"):
    while True:
        # os system('cls') # For Windows OS
        os.system('clear')  # For Linux/OS X
        print(banner)
        Ip = input("\n    -> \033[1;94mIPv6\033[1;m scan - Input, e.g. \033[1;94m2a04:35c0::\033[1;m or \033[1;94m2001:0db8:85a3:0000:8a2e:0370:7334\033[1;m [ENTER]: ")
        try:
            ipaddress.ip_network(Ip)
            print("\n    -> Your \033[1;94mIPv6\033[1;m Addresse to scan is: \033[1;94m" + str(Ip) + "\033[1;m")
            break
        except:
            print("\n    -> Your input has the wrong IP format! " + str(Ip))
            time.sleep(2.0)
            continue
else:
    while True:
        # os system('cls') # For Windows OS
        os.system('clear')  # For Linux/OS X
        print(banner)
        Ip = input("\n    -> \033[1;94mIPv4\033[1;m scan - Input,  e.g. \033[1;94m192.168.1.0/24\033[1;m or \033[1;94m192.168.111.12/32\033[1;m [ENTER]: ")
        try:
            ipaddress.ip_network(Ip)
            print("\n    -> Your \033[1;94mIPv4\033[1;m Addresse to scan is: \033[1;94m" + str(Ip) + "\033[1;m")
            break
        except:
            print("\n    -> Your input has the wrong IP format! " + str(Ip))
            time.sleep(2.0)
            continue

while True:

    # os system('cls') # For Windows OS
    os.system('clear')  # For Linux/OS X
    print(banner)

    nmap_parameter_choice = ()
    nmap_parameter_scanoption = ()
    nmap_script_use = ()

    print("\n    -> Network/Host which will be scanned: \033[1;94m" + str(Ip) + "\033[1;m")
    print(" ")
    print("    -> (\033[1;94m1\033[1;m) NMAP -A               => intensive scan with OS/Service version and top ports")
    print("    -> (\033[1;94m2\033[1;m) NMAP -v -A p1-65535   => intensive long scan with OS/Service version, traceroute,")
    print("                                    all ports, all details")
    print("    -> (\033[1;94m3\033[1;m) NMAP -6               => standard Scan with your given IPv6 address")
    print("    -> (\033[1;94m4\033[1;m) NMAP -F -T5           => fast scan with standard ports")
    print("    -> (\033[1;94m5\033[1;m) NMAP <no Parameter>   => standard Scan with top ports only")
    print("    -> (\033[1;94m6\033[1;m) NMAP -d9              => debug scan with highest level. Duration can be very long!")
    print("    -> (\033[1;94m7\033[1;m) NMAP -sV --script     => script Scan to find exploits etc.")
    print("                                    Note: scripts have the *.nse format and can normally find")
    print("                                    in folders like: ~/.nmap/scripts or /usr/share/nmap/scripts")
    print("                                    Update new *.nse scripts: \"$ sudo nmap --script-updatedb\"")

    nmap_parameter_choice = input('\n    -> Which NMAP scan process you would like to use? [Press \033[1;94m1, 2, 3, 4, 5, 6 or 7\033[1;m, then ENTER] ')

    if nmap_parameter_choice == "1":
        print("\n    -> You would like do a \"\033[1;94mNMAP -A\033[1;m\" scan.")
        nmap_parameter_scanoption = ("-v2 -A")
        time.sleep(2.0)
        break

    elif nmap_parameter_choice == ("2"):
        print("\n    -> You would like do a \"\033[1;94mNMAP -v -A p1-65535\033[1;m\" scan.")
        nmap_parameter_scanoption = ("-v2 -A p1-65535")
        time.sleep(2.0)
        break

    elif nmap_parameter_choice == ("3"):
        print("\n    -> You would like do a \"\033[1;94mNMAP -6\033[1;m\" scan.")
        nmap_parameter_scanoption = ("-v2 -6")
        time.sleep(2.0)
        break

    elif nmap_parameter_choice == ("4"):
        print("\n    -> You would like do a \"\033[1;94mNMAP -F -T5\033[1;m\" scan.")
        nmap_parameter_scanoption = ("-v2 -F -T5")
        time.sleep(2.0)
        break

    elif nmap_parameter_choice == ("5"):
        print("\n    -> You would like to start \"\033[1;94mNMAP\033[1;m\" without parameters.")
        nmap_parameter_scanoption = ("-v2")
        time.sleep(2.0)
        break

    elif nmap_parameter_choice == ("6"):
        print("\n    -> You would like do a \"\033[1;94mNMAP -d9\033[1;m\" scan.")
        nmap_parameter_scanoption = ("-v2 -d9")
        time.sleep(2.0)
        break

    elif nmap_parameter_choice == ("7"):
        # os system('cls') # For Windows OS
        os.system('clear')  # For Linux/OS X
        print(banner)

        nse_files = [f for f in os.listdir(nmap_script_pfad) if f.endswith('.nse')]
        print("\n    -> You would like do a \"\033[1;94mNMAP -sV --script\033[1;m\" scan.")
        print("")
        print("    -> Would you like to display the NSE files? (Attention: file liste can be huge)? ")
        wahl = input("       Press (\033[1;94mY\033[1;m or \033[1;94my\033[1;m) then ENTER to display files or just press ENTER to input the script directly. ")
        while True:
            if wahl == ("Y") or wahl == ("y"):
                cli = cmd.Cmd()
                cli.columnize(nse_files, displaywidth=124)
                while True:
                    print("\n--------------------------------------------------------------------------------------")
                    print("\n    > > > Which Script would you like? (enter just the name (no .nse!)                 ")
                    nmap_script_use = input("-------------------------------------------------------------------------------------- \033[1;94m-=>\033[1;m ")
                    nmap_parameter_scanoption = ("-v2 -sV --script " + str(nmap_script_use) + ".nse")
                    my_file = pathlib.Path(str(nmap_script_pfad) + str(nmap_script_use) + ".nse")
                    if my_file.exists ():
                        print("    -> Script-Name \033[1;94m" + str(nmap_script_use) + "\033[1;m is valid.")
                        break
                    else:
                        print("    -> !!! Script name \033[1;94m" + str(nmap_script_use) + "\033[1;m is not valid !!!")
                        continue

                time.sleep(2.0)
                break
            else:
                while True:
                    nmap_script_use = input("\n    > > > Which Script would you like to use? (enter just the name without .nse!) -> ")
                    nmap_parameter_scanoption = ("-v2 -sV --script " + str(nmap_script_use) + ".nse")
                    my_file = pathlib.Path(str(nmap_script_pfad) + str(nmap_script_use) + ".nse")
                    if my_file.exists():
                        print("    -> Script name \033[1;94m" + str(nmap_script_use) + "\033[1;m is valid.")
                        break
                    else:
                        print("    -> !!! Script name \033[1;94m" + str(nmap_script_use) + "\033[1;m is not valid !!!")
                        continue

                time.sleep(2.0)
                break
        break
    else:
        print("\n    -> Your input is wrong! Please just use \033[1;94m1, 2, 3, 4, 5, 6 or 7\033[1;m, as input! ")
        time.sleep(2.0)
        continue

while True:

    # os system('cls') # For Windows OS
    os.system('clear')  # For Linux/OS X
    print(banner)

    nmap_output_choice = ()
    nmap_output_format = ()

    print("\n    -> Network/Host which will be scanned: \033[1;94m" + str(Ip) + "\033[1;m")
    print("    -> NMAP will starts with this command and/or script: \033[1;94m" + str(nmap_parameter_scanoption) + "\033[1;m")
    print("")
    print("    Outputformat:\n")
    print("    -> (\033[1;94m1\033[1;m) NMAP -oN         => standard output format")
    print("    -> (\033[1;94m2\033[1;m) NMAP -oS         => s|<rIpt kIddi3 output format")
    print("    -> (\033[1;94m3\033[1;m) NMAP -oG         => grepable output format")
    print("    -> (\033[1;94m4\033[1;m) NMAP -oX         => XML output format, must be re-edit when you use multible IP's")
    print("    -> (\033[1;94m5\033[1;m) NMAP -oA         => all output file formats")

    nmap_output_choice = input('\n    -> Which NMAP output format would you like? [Press \033[1;94m1, 2, 3, 4, or 5\033[1;m, then ENTER] -> ')
    
    if nmap_output_choice == "1":
        print("\n    -> You would like \033[1;94mnormal (standard)\033[1;m output format.")
        nmap_output_format = ("-v --open -oN lanlist-")
        time.sleep(2.0)
        break

    elif nmap_output_choice == ("2"):
        print("\n    -> You would like \033[1;94ms|<rIpt kIddi3\033[1;m output format.")
        nmap_output_format = (" --open -oS lanlist-")
        time.sleep(2.0)
        break

    elif nmap_output_choice == ("3"):
        print("\n    -> You would like \033[1;94mgrepable\033[1;m output format.")
        nmap_output_format = (" --open -oG lanlist-")
        time.sleep(2.0)
        break

    elif nmap_output_choice == ("4"):
        print("\n    -> You would like \033[1;94mXML\033[1;m output format.")
        nmap_output_format = (" --open -oX lanlist-")
        time.sleep(2.0)
        break

    elif nmap_output_choice == ("5"):
        print("\n    -> You would like \033[1;94mall\033[1;m output formats.")
        nmap_output_format = (" --open -oA lanlist-")
        time.sleep(2.0)
        break

    else:
        print("\n    -> Your input is wrong! Please just use \033[1;94m1, 2, 3, 4, or 5\033[1;m, as input! ")
        time.sleep(2.0)
        continue

# os system('cls') # For Windows OS
os.system('clear')  # For Linux/OS X
print(banner)

date2 = datetime.now().strftime('%d.%m.%Y-%H:%M:%S')
date3 = datetime.now().strftime('%d%m%Y')
net2 = Ip.split("/", 1)
netO = net2[0]



print("\n    -> Network/Host which will be scanned:: \033[1;94m" + str(Ip) + "\033[1;m")
print("    -> NMAP starts with these parameters: \033[1;94m" + str(nmap_parameter_scanoption) + " " + str(nmap_output_format) + str(netO) + "-" + str(date3) + "\033[1;m")
Aktion = ("nmap " + str(Ip) + " " + str(nmap_parameter_scanoption) + " " + str(nmap_output_format) + str(netO) + "-" + str(date3) + ".txt")
print("")
print("    Overview aktive hosts scans:")
print("    (for MAC-Addresses, start the program, in the same network, as Root or SUDO)")
print("    -----------------------------------------------------------------------------------------------------------")
print("\n    Start: \033[1;94m" + date2 + "\033[1;m")
print("    Command: \033[1;94m" + Aktion + "\033[1;m")
print("\n    scanning .......")
print("    -----------------------------------------------------------------------------------------------------------\n")
os.system(Aktion)
print("")
print("    > > > Scan has been completed! < < < ")
print("")
print("    The scan result will you find in the file: \033[1;94m" + "lanlist-" + str(netO) + "-" + str(date3) + ".txt \033[1;m")
print("")
