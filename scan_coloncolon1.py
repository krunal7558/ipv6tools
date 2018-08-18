#!/usr/bin/python

from netaddr import *
import argparse
from scapy.all import *

def main():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)
    # Parse and validate arguments and print usage information
    parser = argparse.ArgumentParser(prog = 'scan_coloncolon1.py' , formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--I' , type = str , help = 'File with list of prefixes to scan one per line')
    parser.add_argument('--O', type = str , help = 'Output file with list of ::1 IP that responds to ping')
    args = vars(parser.parse_args())
    with open(args['I']) as fh:    # open file with list of /40 prefixes per line
        for line in fh:
            logging.debug("Scanning " + line.strip() + " block.")
            net48 = list(IPNetwork(line.strip()).subnet(48))
            for each48 in net48:   # iterate over each /48 prefixes
                net56 = list(each48.subnet(56))
                for each56 in net56: #iterate over each /56 prefixes
                    net64 = list(each56.subnet(64))
                    wfh = open(args['O'],'a')   # open file in append mode
                    for each64 in net64:  # iterate over each /64 prefixes
                        # select first ::1 IP and ping it with timeout to half a second
                        logging.debug("sending ping to " + str(each64[1]))
                        ans = sr1(IPv6(dst=str(each64[1]))/ICMPv6EchoRequest(),timeout=0.5)
                        if ans and ans[IPv6].src == str(each64[1]):   # Ensure reply comes from same source to filter ICMP destination unreachable messages
                           logging.debug("Received reply from " + ans[IPv6].src)
                           wfh.write('\n'+str(each64[1]))    # Write source IP of the packet
                    wfh.close()   # close the file handle at the end of scanning /56 block

if __name__ == "__main__":
    main()



