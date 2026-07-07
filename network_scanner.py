import socket
import ipaddress
from scapy.all import ARP, Ether, srp
from manufacturer import get_manufacturer
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

        try:
            hostname = socket.gethostbyaddr(received.psrc)[0]
        except:
            hostname = "Unknown"

        devices.append({
            devices.append({
    "hostname": hostname,
    "manufacturer": get_manufacturer(received.hwsrc),
    "ip": received.psrc,
    "mac": received.hwsrc
})
        })

    return devices