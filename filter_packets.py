import os
import sys
import re
import linecache

#create output file with only Echo Requests and Replys
def filter(pcapFile, filteredFile):
    print("FILE: " + pcapFile)
    print("called filter function in filter_packets.py for file ")
    outf = open(filteredFile, "w")

    with open(pcapFile, 'rt') as f:
        occurences = []
        #for every line in file, check to see if ping is in line, if it is write it to the new output file.
        for num, line in enumerate(f, 1):
            if "ping" in line:
                #print 'found at line', num
                occurences.append(num)
                outf.write(linecache.getline(pcapFile, num))
