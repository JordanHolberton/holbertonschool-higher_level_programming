#!/usr/bin/python3
'''API Security and Authentication Techniques'''
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    create_access_token,
    get_jwt_identity,
    jwt_required,
    JWTManager,
)


# Dictionary to store user data with hashed passwords
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("admin_password"),
        "role": "admin"
    }
}


# Initialize Flask app and HTTPBasicAuth
app = Flask(__name__)
auth = HTTPBasicAuth()


# Function to verify password for basic authentication
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


# Public route to display a welcome message
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Protected route that requires basic authentication
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# Set the secret key for JWT
app.config["JWT_SECRET_KEY"] = "my_secret_key"
jwt = JWTManager(app)


# Route to handle user login and return a JWT
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Bad username or password"}), 401


# Protected route that requires a valid JWT
@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


# Protected route with role-based access control for admin only
@app.route("/admin-only")
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()

    # Check if the user exists in the users dictionary
    if current_user not in users:
        return jsonify({"error": "User not found"}), 404

    # Check if the user's role is 'admin'
    if users[current_user]['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200


# Error handlers for various JWT errors
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


# Main entry point to run the Flask application
if __name__ == '__main__':
    app.run()
