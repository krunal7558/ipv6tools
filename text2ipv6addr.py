#!/usr/bin/python3
import logging
import ipaddress

ipv6_hmap = {
'o': '0',
'@': 'a',
'!': '1',
'O': '0',
'S': '5',
's': '5',
'I': '1',
'i': '1',
'L': '1',
'l': '1',
'k': 'c',
'K': 'C',
'R': '7',
'r': '7',
'G': '6',
'g': '9',
'Z': '2',
'z': '2'
}



ipv6_chars = (
'0','1','2','3','4','5','6','7','8','9',
'a','b','c','d','e','f',
'A','B','C','D','E','F'
)

def text2ipv6addr(text):
   logging.debug('Calling text2ipv6addr()')
   ipv6_list = []
   ipv6_oct = []
   final_list = []
   for char in list(text):
      if len(ipv6_list) >= 8:
         logging.debug(':'.join(ipv6_list))
         final_list.append(ipaddress.ip_address(':'.join(ipv6_list)))
         ipv6_list = []
      if len(ipv6_oct) >= 4:
         ipv6_list.append(''.join(ipv6_oct))
         ipv6_oct = []
      if char in ipv6_hmap:
         ipv6_oct.append(ipv6_hmap[char])
      elif char in ipv6_chars:
         ipv6_oct.append(char)
      else:
         #discard that char
         pass
   if len(ipv6_list) < 8:
      logging.debug(':'.join(ipv6_list))
      ipv6_list.append(':')
      final_list.append(ipaddress.ip_address(':'.join(ipv6_list)))
   return final_list

if __name__ == '__main__':
   logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)
   text = input("Enter text here: ")
   for address in text2ipv6addr(text):
      print(address.exploded)
