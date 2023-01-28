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
def get_id(request_id):
    data = read_db()

    ##parsing the dictionary users from our json file

    for user in data['users']:
    #using the if else condition to show that user exists.

        user_id = user['id']

        if user_id == request_id:
            return user

    return f"ID" + "\n" + request_id + "\n" + "does not exist"
    return user_id


# @app.route('/v1/users/<id>', methods=['DELETE'])
# def del_id(id):
#     data = read_db()

#     for user in data['users']:


    # for users in enumerate(data):

        # for alpha in users.items():
        #     print(alpha)
        #     if alpha == id_enter:
        #         return users
        #     else:
        #         return "Error"

        user_id = user["id"]

        new_data = []

        if user_id == user['id']:
            data['users'].remove(user)

            new_data.append(user)
            return new_data
        else:
            return "Wrong ID"












# @app.route('/v1/users/<id>')

    ## .load
# def write_db():

#     ## .dump
