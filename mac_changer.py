#!/usr/bin/env python

import subprocess

interface = "bridge0"
new_mac = "00:11:22:33:44:77"

print("[+] Changing MAC address for " + interface + " to " + new_mac)

# subprocess.call("ifconfig en0 down", shell=True)
# subprocess.call("ifconfig bridge0 ether 00:11:22:33:44:55", shell=True)
# subprocess.call("ifconfig en0 up", shell=True)
