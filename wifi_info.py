import subprocess


def get_wifi_info():

    try:

        output = subprocess.check_output(
            "netsh wlan show interfaces",
            shell=True,
            text=True
        )

        info = {
            "ssid": "Not Connected",
            "signal": "Unknown",
            "security": "Unknown",
            "radio": "Unknown"
        }

        for line in output.splitlines():

            if "SSID" in line and "BSSID" not in line:
                info["ssid"] = line.split(":")[1].strip()

            elif "Signal" in line:
                info["signal"] = line.split(":")[1].strip()

            elif "Authentication" in line:
                info["security"] = line.split(":")[1].strip()

            elif "Radio type" in line:
                info["radio"] = line.split(":")[1].strip()

        return info

    except:

        return {
            "ssid": "Unavailable",
            "signal": "Unavailable",
            "security": "Unavailable",
            "radio": "Unavailable"
        }