from scapy.all import *


def getIniatorSAPacket(packets: []) -> scapy.layers.isakmp.ISAKMP:
    return packets[0]

def getResponderSAPacket(packets: []) -> scapy.layers.isakmp.ISAKMP:
    return packets[1]

def getPayloadFromISAKMP(packet: scapy.layers.isakmp.ISAKMP, name: str) -> bytes:
    return packet[name].load

def getCookieFromISAKMP(respPacket: scapy.layers.isakmp.ISAKMP, responderCookie: bool) -> bytes:
    if responderCookie:
        return respPacket["ISAKMP"].resp_cookie
    else:
        return respPacket["ISAKMP"].init_cookie

def getSAPayloadFromInitPacket(packet: scapy.layers.isakmp.ISAKMP) -> bytes: 
    payloadLength = packet["ISAKMP_payload_SA"].length
    return bytes(packet["ISAKMP_payload_SA"])[4:payloadLength]

def getResponderIDFromRespPacket(packet: scapy.layers.isakmp.ISAKMP) -> bytes:
    payloadLength = packet["ISAKMP_payload_ID"].length
    return bytes(packet["ISAKMP_payload_ID"])[4:payloadLength]

def getRespHashfromPacket(packet: scapy.layers.isakmp.ISAKMP) -> bytes:
    return packet["ISAKMP_payload_Hash"].load
