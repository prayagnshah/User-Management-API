# importing flask framework

from flask import Flask, json, request, jsonify
from dotenv import load_dotenv, find_dotenv
import pyrebase
import os
import uuid
import base64
import requests
app = Flask(__name__)


def get_user_ip():
    """
    Getting the IP address of the user
    """
    return requests.get('https://api.ipify.org').text

print(get_user_ip())

# function to decode value


def decode_base64(string):
    return base64.b64decode(string).decode('utf-8')


# This will search for .env file
load_dotenv(find_dotenv())

# Decoding the string value from .env
decoded_value = decode_base64(os.getenv("FIREBASE_CONFIG"))


FIREBASE_CONFIG = json.loads(decoded_value)

firebase = pyrebase.initialize_app(FIREBASE_CONFIG)

db = firebase.database()

# Defining the child name for the read and write database
# child_name = 'users'


def read_db():
    return db.get().val()


# creating the json file in write mode and then adding directly to the firebase

def write_db(updated_database):
    return db.set(updated_database)

# Title of the page


@app.route('/')
def index():
    return 'Welcome to my project'

# Using this endpoint to get the database


@app.route('/v1/users', methods=['GET'])
def read_users():

    data = read_db()
    # To get the query string of name team
    team = request.args.get('team')

    # Printing the whole database if Team is not entered
    if team is None:
        return jsonify(data)

    # storing into empty dictionary
    results = []

    # getting the values of the dictionary and
    # then matching up with team
    for user_value in data.get('users'):
        if user_value.get('team') == team:
            results.append(user_value)

    return jsonify(results)

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

            # Ensure that the user's input does not modify ID
            request_data.pop('id', None)
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
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    print('Flask app is running on port', get_flask_port())



def get_user_ip():
    """
    Getting the IP address of the user
    """
    return requests.get('https://api.ipify.org').text