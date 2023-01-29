##importing flask framework

from flask import Flask, json, request, jsonify
from flask_sqlalchemy import SQLAlchemy
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

@app.route('/')
def index():
    return 'Welcome to my project'

@app.route('/v1/users', methods = ['GET'])
def read_users():
    return read_db()

@app.route('/v1/users', methods = ['POST'])
def write_users():
    db = read_db()
    users = db.get('users')
    new_user = request.json  ##how to get the body in postman
    users.append(new_user)  ##how to write new information in user
    write_db(db)
    return str(True)

@app.route('/v1/users/<request_id>', methods=['GET'])
def get_employee(request_id):
    data = read_db()
    # user_exist = False

    ##parsing the dictionary users from our json file

    for user in data['users']:
        if user["id"] == request_id:
            # user_exist = True
            return jsonify({'name': user['name']})

    return jsonify({'error': 'User with id does not exist'})
