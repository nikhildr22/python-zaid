#!/usr/bin/python3
'''
Getting the value for  the interface and mac addr to a variable and 
then pass the value to the command directly
secure code
handling user input if the user put ; or && to execute another command 
it will stop by removin the shell=True single string commmand
rather we remove the shell=True and exec the computer and get command 
in a list variable one by one which will avoid this user-input manipulation
'''
'''
we can give value in as a argument in a command line using sys modules 
or with an option with help and switch we use optparse module 
python macchanger.py --interface wlan0 --mac 11:aa:dd:ff:gg:hh
python macchanger.py --help to print help'''

import subprocess
import optparse

parser=optparse.OptionParser()  # init the parser object
parser.add_option("-i","--interface",dest="interface",help="Interface to change the mac address")
# adding the options like -i or --interface switches, dest this where the passed values get saved and help display the help msg python macchanger.py --help

parser.add_option("-m","--mac",dest="new_mac",help="add new mac address")

(options,arguments)=parser.parse_args()	
# the funtion returns a value to this 2 varible options and arguments
# options is nothing but the wlan0 and aa:bb:cc:dd:ee:ff
# arguments is nothing but --interface and --mac or -i and -m

interface = options.interface
macaddr = options.new_mac

# options contain the value to get the value we call options.interface and options.new_mac

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",macaddr])
subprocess.call(["ifconfig",interface,"up"])

print(f"[+] Changing Mac Address of Interface {interface} to {macaddr}")