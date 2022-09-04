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

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), unique = True)
    age = db.Column(db.Integer)
    team = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.age} - {self.team}"

@app.route('/')
def index():
    return 'Hello'

@app.route('/vi/users')
def vi():
    users = Drink.query.all()
    output = []

    for sec in users:
        users_data = {'id': sec.id, 'name': sec.name, 'age': sec.age, 'team': sec.team}
        output.append(users_data)

    return {"users": output}

@app.route('/vi/users/<id>')
def user_id(id):
    sec = Drink.query.get_or_404(id)

    # if sec is None:
    #     return {"error": "user with <id> does not exist"}

    ##dictionaries are seriliazable
    return {'id': sec.id, 'name': sec.name, 'age': sec.age, 'team': sec.team}

#     ##dictionaries are easily seriationalizable
#     return f"{'id': sec.id, 'name': sec.name, 'age': sec.age, 'team': sec.team}

# @app.route('/vi/users', methods = ['POST'])
# def add_data():
#     sec = Drink(id=request.json['id'], name = request.json['name'])
#     db.session.add(sec)
#     db.session.commit()
#     return {'id': sec.id, 'name': sec.name}

##Deleting a record from the field

@app.route('/vi/users/<id>', methods=['DELETE'])
def delete_id(id):
    sec = Drink.query.get(id)
    if sec is None:
        return {"error": "404 Not found"}
    db.session.delete(sec)
    db.session.commit()
    return {"message": "Done"}

# @app.route('/vi/users/<id>', methods=['PUT'])
# def insert_data():
#     sec = Drink.query.get(id)
#     db.session.add(sec)
#     db.session.commit()
