from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

app.config['JWT_SECRET_KEY'] = 'jemmerdeAnzo'
jwt = JWTManager(app)

auth = HTTPBasicAuth()

users ={
    "user1": {"username": "user1", "password": generate_password_hash("hello"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("bye"), "role": "admin"}
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
    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        acces_token = create_access_token(identity={
            "username": username,
            "role": user['role']
            })
        return jsonify({"message": "Access Granted"}), 200


@app.route('/jwt-protect', methods=['GET'])
@jwt_required()
def jwt_protect():
    current_user = get_jwt_identity()
    return jsonify({
        "message": "JWT Auth: Access Granted",
        "user" : current_user
    })


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():

    current_user = get_jwt_identity()

    if current_user['role'] not in 'admin':
        return jsonify({"error": "Forbidden"}), 403

    return jsonify({"message": "Admin Access: Granted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
