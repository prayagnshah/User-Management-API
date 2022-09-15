##importing flask framework

from flask import Flask, json, request, abort
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


##importing flask data to database table


##copied from the flask documentation for sqlalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
##ORM joining the model through sqlalchemy
##Object relational mapper


def read_db():
    with open('database.json', 'r') as f:
        data = json.load(f)
        return data


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
    users.append(request.json)
    write_db(db)
    return str(True)

@app.route('/v1/users/<request_id>', methods = ['GET'])
def get_id(request_id):
    data = read_db()

    ##parsing the dictionary users from our json file

    for users_id in data['users']:
    #using the if else condition to show that user exists.

        id_users = users_id['id']

        if id_users == request_id:
            return id_users

    return f"Hello"












# @app.route('/v1/users/<id>')

    ## .load
# def write_db():

#     ## .dump