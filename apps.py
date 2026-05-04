from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/create_user", methods=["POST"])
def create_user():
    return jsonify(message="User created successfully!"), 201


@app.route("/get_user", methods=["GET"])
def get_user():
    return jsonify(message="User details retrieved successfully!"), 200

@app.route("/update_user", methods=["PUT"])
def update_user():
    return jsonify(message="User updated successfully!"), 200

@app.route("/delete_user", methods=["DELETE"])
def delete_user():
    return jsonify(message="User deleted successfully!"), 200

if __name__ == "__main__":
    app.run(debug=False, port=5013)