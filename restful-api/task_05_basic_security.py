#!/usr/bin/env python
""" Basic security with Flask-JWT-Extended """


from flask import Flask, jsonify, request

from flask_httpauth import HTTPBasicAuth

from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_jwt_extended import jwt_required, JWTManager

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@app.route("/basic_protected", methods=["GET"])
@auth.login_required
def basic_security():
    """ Basic Auth protected route """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """ Login route """
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify(), 400
    user = users.get(username, None)
    if not user or not check_password_hash(user["password"], password):
        return jsonify(), 401
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_security():
    """ JWT protected route """
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """ Admin only route """
    current_user = get_jwt_identity()
    user = users.get(current_user)
    if user["role"] == "admin":
        return "Admin Access Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
