from flask import Flask, jsonify, request

app = Flask(__name__)

users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route('/')
def home():
    """Return a welcome message at the root URL"""
    return "Welcome to the Flask API!"

@app.route('/data')
def get_usernames():
    """Return a JSON list of all usernames stored in the API"""
    usernames = list(users.keys())
    return jsonify(usernames)

@app.route('/status')
def status():
    """Return OK status"""
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """Return the user details for the given username"""
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user to the users dictionary"""
    new_user_data = request.get_json()

    username = new_user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": new_user_data.get("name"),
        "age": new_user_data.get("age"),
        "city": new_user_data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run()
