#!/usr/bin/python3
""" """

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

if __name__ == "__main__":
    app.run()

users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

@app.route('/data')
def current_users():
    return jsonify(list(users.keys()))

@app.route('/status')
def return_status():
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    user = request.get_json()

    username = user.get("username")

    users[username] = {
        "name": user.get("name"),
        "age": user.get("age"),
        "city": user.get("city")
    }

    return ("{} has been added successfully".format(username))