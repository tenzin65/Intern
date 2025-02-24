from scapy.all import rdpcap
pkts_list = rdpcap(r"D:\\Wireshark\\intern\\tcp.pcapng")
print(pkts_list.summary())