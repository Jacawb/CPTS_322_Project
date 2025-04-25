import json
import os
from flask import Flask, request, jsonify, render_template
from passlib.hash import pbkdf2_sha256 as hasher

# Globals
app = Flask(__name__, template_folder='templates')
DATA_FILE = "data.json"

# User-data Format (Dictionary)
# {
#     username : {
#         password: "password",
#         lists: [list1, list2, ...]
#     }
# }



# Create dictionary with data from the json data file.
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}  # Empty dict if no file


# Write data dictionary to json file.
def save_json(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)


# Create data dictionary
data = load_data()



# Create new user account
@app.route("/new_user", methods=["POST"])
def new_user():
    req = request.json
    print(request.data)
    print(request.is_json)

    username = req.get("username")
    password = req.get("password")

    # Error Checks
    if not username or not password:
        return jsonify({"error": "Username and/or password not provided."}), 400
    if username in data:
        return jsonify({"error": "Username taken"}), 400

    hashed_password = hasher.hash(password)  # Hash password
    data[username] = {
        "password": hashed_password,
        "lists": []  # No reading lists upon account creation
    }
    save_json(data)
    return jsonify({"message": f"User '{username}' registered successfully."}), 201


# Login to existing account
@app.route("/login", methods=["POST"])
def login():
    req = request.json
    username = req.get("username")
    password = req.get("password")

    # Check for proper authentication
    user = data.get(username)
    if not user:
        return jsonify({"error": "Invalid username."}), 401
    if not hasher.verify(password, user["password"]):
        return jsonify({"error": "Incorrect password."}), 401

    return jsonify({"message": f"User '{username}' logged-in successfully."}), 200


# Render HTML
@app.route("/")
def home():
    return render_template('frontend.html')



if __name__ == "__main__":
    app.run(debug=True)
