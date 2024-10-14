from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

# Initialize Flask application
app = Flask(__name__)

# JWT secret key for token generation and validation
app.config['JWT_SECRET_KEY'] = "123456azerty"

# Initialize JWT manager with app
jwt = JWTManager(app)

# Initialize basic authentication
auth = HTTPBasicAuth()

# In-memory users' data with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("hello"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("bye"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 401

    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={
            "username": username,
            "role": user['role']
        })
        return jsonify({
            "message": "Access Granted",
            "access_token": access_token
        }), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protect', methods=['GET'])
@jwt_required()
def jwt_protect():
    current_user = get_jwt_identity()
    return jsonify({
        "message": "JWT Auth: Access Granted",
        "user": current_user
    }), 200


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"error": "Forbidden"}), 403
    return jsonify({"message": "Admin Access: Granted"}), 200


# Custom error handlers for JWT issues
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
    app.run(debug=True)
