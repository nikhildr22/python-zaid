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

import subprocess

interface = input("Interface> ")
macaddr = input("MacAddr> ")

print(f"[+] Changing Mac Address of Interface {interface} to {macaddr}")


subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",macaddr])
subprocess.call(["ifconfig",interface,"up"])

print(f"[+] Successfully changed Mac Address of Interface {interface} to {macaddr}")