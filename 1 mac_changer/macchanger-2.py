#!/usr/bin/python3
'''
Storing the interface and mac addr to a variable and 
then pass the value to the command directly
'''

import subprocess

interface = "wlan0"
macaddr = "00:11:22:33:44:55"

print(f"[+] Changing Mac Address of Interface {interface} to {macaddr}")


subprocess.call(f"ifconfig {interface} down",shell=True)
subprocess.call(f"ifconfig {interface} hw ether {macaddr}",shell=True)
subprocess.call(f"ifconfig {interface} up",shell=True)