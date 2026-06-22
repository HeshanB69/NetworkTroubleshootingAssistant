import subprocess
import socket

def check_internet():
    try:
        result = subprocess.run(
            ["ping", "8.8.8.8", "-n", "1"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return "Internet Connected"

        return "Internet Disconnected"

    except Exception as e:
        return f"Error: {e}"


def get_ip_address():
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)

        return ip

    except Exception as e:
        return f"Error: {e}"
    
def check_dns():
    try:
        ip = socket.gethostbyname("google.com")
        return f"DNS Working ({ip})"

    except Exception as e:
        return f"DNS Failed: {e}"



print("IP Address:", get_ip_address())
print("Internet Status:", check_internet())
print("DNS Status:", check_dns())