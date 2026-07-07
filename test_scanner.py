from network_scanner import scan_network

devices = scan_network("192.168.1.0/24")

print("Devices Found")

for device in devices:
    print(device["ip"], device["mac"])