#!/usr/bin/python
from __future__ import print_function

#Q7) MacAddressToBitString :
#
#    Write a function that accepts a MAC address in human-friendly string as the input and outputs a string of bits representing that mac address. Assume that the MAC-48 address will be a string of the format :
#        [0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]:[0-9A-F][0-9A-F]
#        ie: 6 groups of 2 digits each with each digit ranging from zero to nine or A to F, for a total length of 48 bits.
#        Sample Tests
#        Sr No   Input   Expected Output
#        1   00:00:00:00:00:11   000000000000000000000000000000000000000000010001
#        2   00:00:00:01:01:03   000000000000000000000000000000010000001000000011
#        3   03:FF:00:01:A2:3F   000000111111111100000000000000011010001000111111
#        Note that the length of the binary string representation will always be 48 since a MAC address is that many bits long.
#
#
#        --------------------------------------------------------------------------------
#

import sys

mapping = { '0':'0000','1':'0001','2':'0010','3':'0011','4','0100','5','0101','6':'0110','7':'0111','8':'1000','9':'1001','A':'1010','B':'1011','C':'1100','D':'1101','E':'1110','F':'1110' }

def macaddress_to_bitstring(mac):
    bitstring = ""
    for parts in mac.split(":"):
        part0,part1 = parts[0],parts[1]
        bitstring += mapping[part0] + mapping[part1]

    return bitstring

if __name__ == "__main__":
    print(macaddress_to_bitstring(sys.argv[1]))
