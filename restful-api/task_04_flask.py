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

@app.route('/status')
def return_status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    return jsonify(users[username])

