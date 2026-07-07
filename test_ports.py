from port_scanner import scan_ports

ip = input("Enter IP Address: ")

results = scan_ports(ip)

for port in results:
    print(
        f"{port['port']} ({port['service']}) : {port['status']}"
    )