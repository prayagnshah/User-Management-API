import json

def read_db():
    with open('database.json', 'r') as f:
        data = json.load(f)
        return data

def del_id(id_enter):
    data = read_db()

    # for users in data['users']:
    for users in enumerate(data):
        print(users)