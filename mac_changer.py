#!/usr/bin/env python

import subprocess
import time

def current_mac(adapter):
    print("[+] Current MAC address :")
    subprocess.call(["ifconfig "+adapter+" | grep ether  | awk '{print $2}'"], shell=True)

def current_mac1(adapter):
    subprocess.call(["ifconfig "+adapter+" | grep ether  | awk '{print $2}'"], shell=True)

def available_interfaces():
	print("[+] Available Interfaces")
	subprocess.call(["netstat -i | awk '{print $1}'| grep -v Iface | grep -v ernel"], shell=True)	
	
def mac_changer(adapter,new_mac):
	print("[+] Changing MAC address .... ")
	subprocess.call("ifconfig eth0 down", shell=True)
	subprocess.call(["ifconfig "+adapter+" hw ether "+ new_mac],shell=True)
	subprocess.call(["ifconfig "+adapter+" up"],shell=True)

def main():
	available_interfaces()
	adapter = input("Enter the adapter :")
	current_mac(str(adapter))	
	new_mac = input("Enter the new MAC address Eg :- (00:0c:29:6f:36:31) \n")	
	try:
		mac_changer(adapter,new_mac)
	except: 
		print("Invalid MAC")
	print("[+] Changed MAC address for " + adapter + " to ")
	current_mac1(adapter)

main()

