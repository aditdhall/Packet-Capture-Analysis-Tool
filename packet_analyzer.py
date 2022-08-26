from filter_packets import *
from packet_parser import *
from compute_metrics import *

#call all functions with specified information.
if __name__ == "__main__":
    pcap = "Node1.txt"
    filteredFile = "Node1_filtered.txt"
    filter(pcap, filteredFile)
    packet = parse(filteredFile)
    ipAddr = "192.168.100.1"
    compute(packet, ipAddr)

    pcap = "Node2.txt"
    filteredFile = "Node2_filtered.txt"
    filter(pcap, filteredFile)
    packet = parse(filteredFile)
    ipAddr = "192.168.100.2"
    compute(packet, ipAddr)

    pcap = "Node3.txt"
    filteredFile = "Node3_filtered.txt"
    filter(pcap, filteredFile)
    packet = parse(filteredFile)
    ipAddr = "192.168.200.1"
    compute(packet, ipAddr)

    pcap = "Node4.txt"
    filteredFile = "Node4_filtered.txt"
    filter(pcap, filteredFile)
    packet = parse(filteredFile)
    ipAddr = "192.168.200.2"
    compute(packet, ipAddr)
