# ipv6tools

## text2ipv6addr.py:

**NAME**
    text2ipv6addr

**FUNCTIONS**

    text2ipv6addr(text)
        This function takes a text string as input and map each charactor based on ipv6_hmap dictionary
        This function returns a list of IPv6Adress objects which can be interate over to print a
        address per line or pipe to another IPv6 command sets

**DATA**

    ipv6_chars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', '...
    ipv6_hmap = {'!': '1', '@': 'a', 'G': '6', 'I': '1', 'K': 'C', 'L': '1...

## scan_coloncolon1.py: 

IPv6 address scanner for ::1 addresses out of /40 or /48 prefixed specified in file. 

	usage: scan_coloncolon1.py [-h] [--I I] [--O O]
	
	optional arguments:
	  -h, --help  show this help message and exit
	  --I I       File with list of prefixes to scan one per line (default: None)
	  --O O       Output file with list of ::1 IP that responds to ping (default:
	              None)

## ipv6_addr_parsing.py

This program takes an IPv6 address as input and returns a list of 8 HEX numbers. Zero compression and zero suppression is not implemented.
