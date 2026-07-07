from flask import Flask, render_template
from connectivity import *

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "ip": get_ip_address(),
        "internet": check_internet(),
        "dns": check_dns(),
        "gateway": get_gateway(),
        "gateway_status": check_gateway(),
        "recommendation": get_recommendation()
    }

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)