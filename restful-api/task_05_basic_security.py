from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity

# Initialize Flask application
app = Flask(__name__)

# JWT secret key for token generation and validation
app.config['JWT_SECRET_KEY'] = 'jemmerdeAnzo'

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
    """
    Verifies if the username exists and if the provided password
    matches the stored hashed password.

    :param username: Username string from request
    :param password: Password string from request
    :return: User dictionary if password is correct, None otherwise
    """
    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        return user
    return None


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Route protected by basic authentication. Returns success message
    if valid credentials are provided.

    :return: JSON response with success message and HTTP 200 status
    """
    return jsonify({"message": "Basic Auth: Access Granted"}), 200


@app.route('/login', methods=['POST'])
def login():
    """
    Route for user login. Accepts JSON payload with username and password,
    validates credentials, and returns a JWT token if successful.

    :return: JSON response with JWT token if credentials are valid
    """
    username = request.json.get('username')
    password = request.json.get('password')
    user = users.get(username)

    # Check if user exists and password is correct
    if user and check_password_hash(user['password'], password):
        # Create JWT access token with user identity and role
        acces_token = create_access_token(identity={
            "username": username,
            "role": user['role']
        })
        return jsonify({
            "message": "Access Granted", "access_token": access_token
            }), 200

    # Return unauthorized response if credentials are invalid
    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protect', methods=['GET'])
@jwt_required()
def jwt_protect():
    """
    Route protected by JWT authentication. Returns success message
    and user information if a valid JWT token is provided.

    :return: JSON response with success message and user details
    """
    current_user = get_jwt_identity()

    return jsonify({
        "message": "JWT Auth: Access Granted",
        "user": current_user
    }), 200


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Admin-only route protected by JWT. Returns success message if the
    user is an admin. Otherwise, returns a forbidden error.

    :return: JSON response with success message for admins,
    forbidden error for others
    """
    current_user = get_jwt_identity()

    # Check if the current user has 'admin' role
    if current_user['role'] != 'admin':
        return jsonify({"error": "Forbidden"}), 403

    return jsonify({"message": "Admin Access: Granted"}), 200


if __name__ == "__main__":
    # Run the Flask application in debug mode
    app.run(debug=True)
