from port_scanner import scan_ports
from wifi_info import get_wifi_info
from speed_test import run_speed_test
from public_ip import get_public_ip
from network_scanner import scan_network, get_network
from flask import request
from flask import Flask, render_template
from connectivity import *

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
        "devices": scan_network(get_network()),
        "wifi": get_wifi_info(),
      
    }

    return render_template("index.html", data=data)

@app.route("/speedtest")
def speedtest():

    result = run_speed_test()

    return render_template(
        "speedtest.html",
        result=result
    )
@app.route("/portscanner", methods=["GET", "POST"])
def portscanner():

    results = None

    if request.method == "POST":

        ip = request.form["ip"]

        results = scan_ports(ip)

        return render_template(
            "portscanner.html",
            results=results,
            ip=ip
        )

    return render_template(
        "portscanner.html",
        results=None
    )

if __name__ == "__main__":
    app.run(debug=True)