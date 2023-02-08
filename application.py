# importing flask framework

from flask import Flask, json, request, jsonify
import os
import uuid
app = Flask(__name__)

# reading the json file


def read_db():
    with open('database.json', 'r') as f:
        data = json.load(f)
        return data

# creating the json file in write mode


def write_db(updated_database):
    with open('database.json', 'w') as f:
        json.dump(updated_database, f, indent=2)

# Title of the page


@app.route('/')
def index():
    return 'Welcome to my project'

# Using this endpoint to get the database


@app.route('/v1/users', methods=['GET'])
def read_users():
    return read_db()

# Using the endpoint to retrieve the data
# once the user enters the ID from database


@app.route('/v1/users/<request_id>', methods=['GET'])
def get_employee(request_id):
    data = read_db()

    # parsing the dictionary users from our json file
    # using GET function in order to save the system from
    # throwing an error from the database

    for user in data.get('users'):
        if user.get('id') == request_id:

            return jsonify(user)

    return jsonify({'error': 'User with {} does not exist'.format(request_id)}), 404


# Using this endpoint to delete the data as soon as the ID is entered
@app.route('/v1/users/<request_id>', methods=['DELETE'])
def delete_id(request_id):
    data = read_db()

    # index variable will store all json names and user will
    # store the ID matcing the names
    for index, user in enumerate(data['users']):
        if user.get('id') == request_id:
            del data['users'][index]

            # writing the file back to database
            write_db(data)

            return jsonify({'result': 'User with id {} deleted successfully'.format(request_id)})

    return jsonify({'error': 'User with {} does not exist'.format(request_id)}), 404

# Using this endpoint to create the POST request to add the new user
# into the database


@app.route('/v1/users', methods=['POST'])
def add_user():
    required_keys = ['name', 'age', 'team']
    # requesting input in json format
    request_data = request.get_json()

    # storing key values from the user
    user_key = {}

    # storing missing keys and producing error
    missing_keys = []

    for key in required_keys:
        if key not in request_data:
            missing_keys.append(key)

    if missing_keys:
        return jsonify({"error": "Cannot create user as following attributes are missing:{}".format(",".join(missing_keys))}), 400

    # storing the user entered values
    for key in required_keys:
        user_key[key] = request_data[key]

    # creating random ID
    user_key['id'] = str(uuid.uuid4())

    data = read_db()

    # appending to the current database
    data['users'].append(user_key)
    write_db(data)

    # showing output message according to the card
    return jsonify({'message': 'User added successfully'})


# Modifying the users data in database using PUT request

@app.route('/v1/users/<id>', methods=['PUT'])
def modify_user(id):
    data = read_db()

    request_data = request.get_json()

    # modifying the data as per the user's input
    for modify in data.get('users'):
        if modify.get('id') == id:
            modify.update(request_data)
            write_db(data)
            return jsonify(modify)

    # Returning invalid ID
    return jsonify({"error": "User with id {} is invalid".format(id)}), 404


def get_flask_port():
    server_name = app.config.get("SERVER_NAME")
    if server_name:
        _, port = server_name.split(":")
        return port
    else:
        return "5000"


if __name__ == "__main__":
    port = os.environ.get('PORT') or 5000
    print(port)
    app.run(port=port)
    print('Flask app is running on port', get_flask_port())
