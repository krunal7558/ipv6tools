#!/usr/bin/python3

from ipaddress import *

GUA_PREFIX = ip_network('2::/3')
ULA_PREFIX = ipaddress.ip_network('fc::/7')
LLA_PREFIX = ipaddress.ip_network('fe80::/10')
MULTICAST_PREFIX = ipaddress.ip_network('ff::/8')
DOC_PREFIX = ipaddress.ip_network('2001:db8::/32')

def main():
    pass

if __name__ == "__main__":
    main()

