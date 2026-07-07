from public_ip import get_public_ip
from network_scanner import scan_network, get_network
from flask import Flask, render_template
from connectivity import *
from network_scanner import scan_network
app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "ip": get_ip_address(),
        "public_ip": get_public_ip(),
        "internet": check_internet(),
        "dns": check_dns(),
        "gateway": get_gateway(),
        "gateway_status": check_gateway(),
        "recommendation": get_recommendation(),
        "devices": scan_network(get_network())
      
    }

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)