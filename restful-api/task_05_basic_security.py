#!/usr/bin/env python
"""Enhanced Security with Flask-JWT-Extended and Basic Auth"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    create_access_token, get_jwt_identity,
    jwt_required, JWTManager
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret"
jwt = JWTManager(app)
auth = HTTPBasicAuth()
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


@auth.verify_password
def verify_password(username, password):
    """Verify user credentials for Basic Auth"""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username



@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """Basic authentication protected route"""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Login route that generates JWT token upon valid credentials"""
    if not request.is_json:
        return jsonify(), 400

    data = request.get_json()
    username = data.get("username", None)
    password = data.get("password", None)

    if not username or not password:
        return jsonify(), 400

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify(), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """JWT-protected route"""
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Admin only route, accessible to users with the admin role"""
    current_user = get_jwt_identity()
    user = users.get(current_user)

    if user and user["role"] == "admin":
        return "Admin Access: Granted", 200
    else:
        return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    app.run()
