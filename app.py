from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        amount = float(request.form["amount"])
        currency = request.form["currency"]

        if currency in ["USD", "EUR", "RUB"]:
            url = f"https://api.exchangerate.host/latest?base={currency}&symbols=UZS"
            data = requests.get(url).json()
            result = amount * data["rates"]["UZS"]

        elif currency == "BTC":
            data = requests.get(
                "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=uzs"
            ).json()
            result = amount * data["bitcoin"]["uzs"]

        elif currency == "ETH":
            data = requests.get(
                "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=uzs"
            ).json()
            result = amount * data["ethereum"]["uzs"]

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()
