import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "Remote Desktop"
}


def scan_ports(ip):

    results = []

    for port, service in COMMON_PORTS.items():

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((ip, port))

        if result == 0:
            status = "Open"
        else:
            status = "Closed"

        results.append({
            "port": port,
            "service": service,
            "status": status
        })

        sock.close()

    return results