/#! usr/bin/env python


#Using subprocess to execute shell command 
import subprocess

"""
In this instance, a connected virtual ethernetwork is used elan0. Most wireless network interfaces
are called wlan0. To use this tool, you will need to change eth0 to your interface name
To find out the name of your network interface, you can open a terminal (linux) and type ifconfig.
"""

#Switch off the network interface, change the MAC address and switch it back on
subprocess.call("ifconfig elan0 down", shell=True)

#This changes the MAC address to 00:11:22:33:44:66
#You can change this to the address of your choosing, make sure to use 12 characters
subprocess.call("ifconfig elan0 hw ether 00:11:22:33:44:66", shell=True)
subprocess.call("ifconfig elan0 down", shell=True)


