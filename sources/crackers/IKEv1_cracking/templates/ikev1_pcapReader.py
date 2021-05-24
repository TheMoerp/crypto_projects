from scapy.all import *


def openPCAPFile(path: str) -> scapy.plist.PacketList:
    return rdpcap(path)

def getISAKMPPackets(packets: scapy.plist.PacketList) -> []:
    return packets.getlayer(ISAKMP)
