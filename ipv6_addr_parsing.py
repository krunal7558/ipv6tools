##################################################
# Ths program takes an IPv6 address as input and
# returns a list of 8 HEX numbers.  
# Zero compression and zero suppression is not implemented.
##################################################

import pprint
ipv6_addr = input("Enter IPv6 address : " )
ipv6_list = ipv6_addr.split(':')

ipv6_hex = []  # initialize the empty IPV6 hex list
# following line is for debuging purpose to see what is split list we get
#print("Here is splited list:")
#pprint.pprint(ipv6_list)

if (len(ipv6_list) > 8 or ipv6_list.count('')>2):
	print("Invalid address")
	print("Please enter valid IPv6 address")
	exit()
elif (ipv6_list.count('')==2):   # for IPv6 address ::1 case
	ipv6_list.remove('')
if (len(ipv6_list)<=8 and ipv6_list.count('')==1):
	# while length of IPv6 address list is remain greater or equal to 8
	# keep on adding '0'
	while (len(ipv6_list)<=8):
		ipv6_list.insert(ipv6_list.index(''),'0')
	ipv6_list.remove('')
	# under try except block to avoide getting ValueError due user input
	# invalid hex number such as floo:23 OR klp:12345: etc
	try:
		for element in ipv6_list:
			ipv6_hex.append(hex(int(element,16)))
	except(ValueError):
		print("Invalid address")
		print("Please enter valid IPv6 address")
		exit()
print(ipv6_hex)
# when converting this into function uncomment following line
#return ipv6_hex




    

