#!/usr/bin/env python

# Built-in/Generic Imports
import optparse

# Thirdparty imports
import scapy.all as scapy


def scan(ip):
    '''
    Send ARP requests to the broadcast MAC address
    and save all responses into a lsit of dictionaries.
    Each response return both target's IP and MAC address.
    '''

    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_broadcast = broadcast / arp_request
    answers = scapy.srp(arp_broadcast, timeout=2, verbose=False)[0]

    clients_list = []
    for answer in answers:
        clients_dict = {'ip':answer[1].psrc, 'mac':answer[1].hwsrc}
        clients_list.append(clients_dict)
    return clients_list


def print_result(clients_list):
    ''' Print the results of the network scan.'''

    print('IP\t\t\tMAC Address')
    print('-------------------------------------------')
    for client in clients_list:
        print(client['ip'] + '\t\t' + client['mac'])


def get_args():
    '''Get user arguments  and parse them.'''

    usage = "usage: %prog [OPTION1] arg1"
    parser = optparse.OptionParser(usage=usage)
    parser.add_option("-t", "--target", dest="target", help="Specify IP target range")
    (options, arguments) = parser.parse_args()
    if not options.target:
        parser.error("[-] Please specify an IP target range, use --help for more info")
    return options


options = get_args()
scan_result = scan(options.target)
print_result(scan_result)
