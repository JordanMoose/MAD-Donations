from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
import backend.constants as const

app = Flask(__name__)
CORS(app)

client = MongoClient(const.MONGO_URI)
db = client['mad-donations']


@app.route("/")
def hello():
    user = db.users.find_one()
    return user['name']

# Test endpoint to get React, Flask, and Mongo hooked up
@app.route("/getUser/id/<string:id>/")
def getUserById(id):
    user = db.users.find({'_id': id})[0]
    return {
        '_id': str(user['_id']),
        'name': user['name']
    }

@app.route("/getUser/name/<string:name>/")
def getUserByName(name):
    user = db.users.find({'firstName': name})[0]
    return {
        '_id': str(user['_id']),
        'firstName': user['firstName'],
        'lastName': user['lastName']
    }

@app.route("/home/")
def home():
    return "This is the homepage"


@app.route("/login/")
def login():
    return "This is the login page"


@app.route("/account/")
def account():
    return "You shouldn't be here!"


@app.route("/account/<int:id>/")
def getInfo(id):
    return "This is account %s" % id


@app.route("/account/<string:name>/")
def addMember(name):
    post = {
        'name': name,
    }
    user_id = db.users.insert_one(post).inserted_id
    return "Here is user_id: %s" % user_id


@app.route("/orgs/")
def orgs():
    return "Here are all of our orgs"


@app.route("/orgs/<int:id>")
def getOrg(id):
    return "This is organization %s" % id


if __name__ == "__main__":
    app.run()
    client.close()
