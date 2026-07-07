import requests

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org")

        if response.status_code == 200:
            return response.text

        return "Unavailable"

    except Exception as e:
        return f"Error: {e}"