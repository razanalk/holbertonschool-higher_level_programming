#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "my-secret-key"

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


@auth.verify_password
def verify_password(username, password):
    if username in users:
        if check_password_hash(users[username]["password"], password):
            return username
    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return jsonify({
        "message": "Basic Auth: Access Granted"
    })


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={
            "role": users[username]["role"]
        }
    )

    return jsonify({
        "access_token": access_token
    })


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return jsonify({
        "message": "JWT Auth: Access Granted"
    })


@app.route("/admin-only")
@jwt_required()
def admin_only():
    username = get_jwt_identity()

    if users[username]["role"] != "admin":
        return jsonify({
            "error": "Admin access required"
        }), 403

    return jsonify({
        "message": "Admin Access: Granted"
    })


if __name__ == "__main__":
    app.run()
