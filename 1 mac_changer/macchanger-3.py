#!/usr/bin/python3
'''
Getting the value for  the interface and mac addr to a variable and 
then pass the value to the command directly
'''

import subprocess

interface = input("Interface> ")
macaddr = input("MacAddr> ")

print(f"[+] Changing Mac Address of Interface {interface} to {macaddr}")


subprocess.call(f"ifconfig {interface} down",shell=True)
subprocess.call(f"ifconfig {interface} hw ether {macaddr}",shell=True)
subprocess.call(f"ifconfig {interface} up",shell=True)

print(f"[+] Successfully changed Mac Address of Interface {interface} to {macaddr}")