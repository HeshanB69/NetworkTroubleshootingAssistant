import subprocess
import socket
import os

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
    
def get_gateway():
    try:
        output = os.popen("ipconfig").read()

        lines = output.splitlines()

        for i, line in enumerate(lines):
            if "Default Gateway" in line:
                gateway = line.split(":")[-1].strip()

                if gateway and "." in gateway:
                    return gateway

                # Check next line for IPv4 gateway
                if i + 1 < len(lines):
                    next_line = lines[i + 1].strip()
                    if "." in next_line:
                        return next_line

        return "Gateway Not Found"

    except Exception as e:
        return f"Error: {e}"
    


def check_gateway():
    try:
        gateway = get_gateway()

        result = subprocess.run(
            ["ping", gateway, "-n", "1"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return "Reachable"

        return "Unreachable"

    except Exception as e:
        return f"Error: {e}"    

def get_recommendation():
    try:
        internet = check_internet()
        dns = check_dns()
        gateway = check_gateway()

        if "Disconnected" in internet:
            return "❌ No internet connection. Check your router or ISP connection."

        elif "Failed" in dns:
            return "⚠️ DNS issue detected. Try using Google's DNS (8.8.8.8)."

        elif "Unreachable" in gateway:
            return "⚠️ Cannot reach the gateway. Check your Wi-Fi or Ethernet connection."

        else:
            return "✅ No network issues detected."

    except Exception as e:
        return f"Error: {e}"




print("IP Address:", get_ip_address())
print("Internet Status:", check_internet())
print("DNS Status:", check_dns())
print("Gateway:", get_gateway())