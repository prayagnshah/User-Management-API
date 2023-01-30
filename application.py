##importing flask framework

from flask import Flask, json, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid
app = Flask(__name__)


##importing flask data to database table


##copied from the flask documentation for sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
##ORM joining the model through sqlalchemy
##Object relational mapper


#reading the json file
def read_db():
    with open('database.json', 'r') as f:
        data = json.load(f)
        return data

# creating the json file in write mode
def write_db(updated_database):
    with open('database.json', 'w') as f:
        json.dump(updated_database, f, indent = 2)

# Title of the page
@app.route('/')
def index():
    return 'Welcome to my project'

# Using this endpoint to get the database
@app.route('/v1/users', methods = ['GET'])
def read_users():
    return read_db()

# # Using this endpoint to add the new data into the database
# @app.route('/v1/users', methods = ['POST'])
# def write_users():
#     db = read_db()
#     users = db.get('users')
#     new_user = request.json  ##how to get the body in postman
#     users.append(new_user)  ##how to write new information in user
#     write_db(db)
#     return jsonify(str(True))

#Using the endpoint to retrieve the data
# once the user enters the ID from database

@app.route('/v1/users/<request_id>', methods=['GET'])
def get_employee(request_id):
    data = read_db()

    #parsing the dictionary users from our json file
    # using GET function in order to save the system from
    # throwing an error from the database

    for user in data.get('users'):
        if user.get('id') == request_id:

            return jsonify({'name': user['name']})

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

    # requesting input in json format
    request_data = request.get_json()

    # checking the condition if name, age and team are matching
    if 'name' in request_data and 'age' in request_data and 'team' in request_data:
        new_user = {
            'id': str(uuid.uuid4()),
            'name': request_data['name'],
            'age': request_data['age'],
            'team': request_data['team']
        }
        data = read_db()

        # appending to the current database
        data['users'].append(new_user)
        write_db(data)

        return jsonify({'message': 'User added successfully'})
    else:
        return jsonify({'error': 'Invalid data, name, age and team are required'}), 400


    # if name in request_data and 'age' in request_data and 'team' in request_data:
    #     new_user = ({ 'name' = request_data['name'], 'age' = request_data['age'], 'team' = request_data['team'] })
    # # requesting data as per the question


    # if not name or not age or not team:
    #     return jsonify({'error': 'Cannot create user as following attributes are missing:'}), 400


    # # if 'name' in request_data and 'age' in request_data and 'team' in request_data:

    # #     new_user = {

    # #     }


