#!/usr/bin/python3
""" """

from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

if __name__ == "__main__":
    app.run()

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route('/data')
def current_users():
    return jsonify(users)