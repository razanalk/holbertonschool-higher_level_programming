#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


def read_json():
    """Read products from the JSON file."""
    with open("products.json", "r") as file:
        return json.load(file)


def read_csv():
    """Read products from the CSV file."""
    with open("products.csv", "r") as file:
        reader = csv.DictReader(file)
        products = []

        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)

        return products


@app.route("/products")
def products():
    """Display products from JSON or CSV."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ["json", "csv"]:
        return render_template(
            "product_display.html",
            products=[],
            error="Wrong source"
        )

    if source == "json":
        products_data = read_json()
    else:
        products_data = read_csv()

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                "product_display.html",
                products=[],
                error="Product not found"
            )

        products_data = [
            product for product in products_data
            if product["id"] == product_id
        ]

        if not products_data:
            return render_template(
                "product_display.html",
                products=[],
                error="Product not found"
            )

    return render_template(
        "product_display.html",
        products=products_data,
        error=None
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
