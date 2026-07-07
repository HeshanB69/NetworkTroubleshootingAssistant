import socket
import ipaddress
from scapy.all import ARP, Ether, srp

def get_network():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    network = ipaddress.IPv4Network(ip + "/24", strict=False)

    return str(network)

def scan_network(network):
    arp_request = ARP(pdst=network)

    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")

    packet = broadcast / arp_request

    answered = srp(packet, timeout=2, verbose=False)[0]

    devices = []

    for sent, received in answered:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices