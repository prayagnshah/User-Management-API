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


@app.route('/')
def index():
    return 'Welcome to my project'

@app.route('/v1/users')
def read_db():
    with open('database.json', 'r') as f:
        data = json.load(f)
        return data

def write_db(updated_database):
    with open('database.json', 'w') as f:
        data_1 = json.dump(updated_database, f)
        return data_1





# @app.route('/v1/users/<id>')

    ## .load
# def write_db():

#     ## .dump