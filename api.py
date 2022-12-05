import json
import requests

URL = "http://127.0.0.1:8000/student/"  # url of the endpoint where data been inputted and save into the database


def get_data(id=None):  # to retrieve the data from the system
    data = {}
    if id is not None:
        data = {'id': id}
    json_data = json.dumps(data)
    r = requests.get(url=URL, data=json_data)
    data = r.json()
    print(data)


# get_data()

def post_data():  # to save the data into the system
    data = {
        'name': "Ajay",
        'department': 'computer science',
        'roll': '12',
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL, data=json_data)
    data = r.json()
    print(data)


# post_data()


def update_data():  # to update the data into the system
    data = {
        'id': "4",
        'name': "mukesh",
        'department': 'computer system',
        'roll': '12',
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL, data=json_data)
    data = r.json()
    print(data)


# update_data()

def delete_data(): # to delete the data into the database
    data = {
        'id': 6}
    json_data = json.dumps(data)
    r = requests.delete(url=URL, data=json_data)
    data = r.json()
    print(data)


delete_data()
