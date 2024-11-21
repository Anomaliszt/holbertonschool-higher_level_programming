#!/usr/bin/python3

from json import load
import csv

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json') as f:
        items = load(f).get('items') or []
    return render_template('items.html', items=items)


@app.route('/products/')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id")
    if source == "json":
        with open('products.json') as f:
            data = load(f)
            items = data
    elif source == "csv":
        with open('products.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            items = [row for row in reader]
    else:
        return render_template('product_display.html',
                               error_message="Wrong source")

    if product_id:
        filtered_items = [item for item in items if str(
            item['id']) == product_id]
        if not filtered_items:
            return render_template('product_display.html',
                                   error_message="Product not found")
        items = filtered_items
    return render_template('product_display.html', items=items)


if __name__ == '__main__':
    app.run(debug=True, port=5000)