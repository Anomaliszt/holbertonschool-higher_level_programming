#!/usr/bin/python3
""" Flask API with GET and POST methods """


from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/')
def home():
    """ Home page """
    return "Welcome to the Flask API!"


users = {{"jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"}, "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}}}


if __name__ == "__main__":
    app.run()
    

@app.route('/data')
def current_users():
    """ Return the list of users """
    return jsonify(list(users.keys()))


@app.route('/status')
def return_status():
    """ Return the status of the API """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """ Return the user details """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """ Add a new user """
    user = request.get_json()

    username = user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = {
        "name": user.get("name"),
        "age": user.get("age"),
        "city": user.get("city")
    }

    return jsonify({
        "message": "User added",
        "user": {
            "username": username,
            "name": user.get("name"),
            "age": user.get("age"),
            "city": user.get("city")
        }
    }), 201


