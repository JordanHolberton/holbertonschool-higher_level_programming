from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory users dictionary to store user data
users = {
    "jane": {
        "username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"
        },
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}


@app.route('/')
def home():
    """
    Root endpoint to return a welcome message.

    This route handles the root URL and provides a welcome message
    when the API is accessed at the root ("/").

    Returns:
        str: A welcome message.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def get_usernames():
    """
    Endpoint to retrieve all usernames stored in the API.

    This route responds to GET requests at "/data" and returns
    a JSON list of all usernames currently stored in the users dictionary.

    Returns:
        Response: A JSON list of usernames.
    """
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route('/status')
def status():
    """
    Endpoint to check the status of the API.

    This route returns a simple "OK" status message when accessed
    via GET request at "/status",
    allowing users to check if the API is running.

    Returns:
        str: Status message "OK".
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Endpoint to retrieve user details by username.

    This route responds to GET requests at "/users/<username>" and
    returns the full details of the user specified by the username.
    If the user is not found, it returns a 404 status with an error message.

    Args:
        username (str): The username to look up.

    Returns:
        Response: A JSON object containing the user's
        details or an error message.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint to add a new user to the users dictionary.

    This route handles POST requests at "/add_user". It parses
    the incoming JSON data to add a new user to the users dictionary,
    using the 'username' field as the key. If the username is missing,
    or if the username already exists, it returns an error.

    Returns:
        Response: A confirmation message with the added user's data,
                  or an error message in case of invalid data.
    """
    new_user_data = request.get_json()

    # Validate that the 'username' field is provided
    username = new_user_data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if the username already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Add the new user to the users dictionary
    users[username] = {
        "username": username,
        "name": new_user_data.get("name"),
        "age": new_user_data.get("age"),
        "city": new_user_data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    # Run the Flask application
    app.run()
