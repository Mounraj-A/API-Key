# app.py

from flask import Flask, render_template, request
from amazon_api import search_products

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    products = []

    if request.method == "POST":
        keyword = request.form.get("keyword")
        products = search_products(keyword)

    return render_template("index.html", products=products)


if __name__ == "__main__":
    app.run(debug=True)