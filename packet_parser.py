import os
import sys
import re

#parse new file and store ICMP packets in an array
def parse(filterFile):
    print 'called parse function in packet_parser.py'
    with open(filterFile, 'rt') as f:
        #create array of packets
        packets = []
        #for all lines in filtered file, add packet to array.
        packets = [line.rstrip("\n") for line in f]
    return packets
