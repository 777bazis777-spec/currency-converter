from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://api.exchangerate-api.com/v4/latest/"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        try:
            amount = float(request.form.get("amount"))
            from_currency = request.form.get("from_currency")
            to_currency = request.form.get("to_currency")

            response = requests.get(API_URL + from_currency)
            data = response.json()

            rate = data["rates"][to_currency]
            result = round(amount * rate, 2)

        except Exception as e:
            error = "Xatolik yuz berdi. Qiymatlarni tekshiring."

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
