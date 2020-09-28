#!/usr/bin/ python3

import subprocess
import re

ifconfig_output = subprocess.check_output(["ifconfig","wlan0"]).decode()
print(ifconfig_output)

mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig_output)

print(f"your MAC address is {mac.group(0)}")