from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt
import spacy


app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://27017")
db = client.SimilarityDB
users = db["Users"]


def UserExist(username):
    """
    Purpose: checks if user is in DB
    """
    if users.find({"Username" :username}).count() == 0:
        return False
    else:
        return True
# end def


class Register(Resource):
    def post(self):
        """
        Purpose: checks username & pwd
        """
        postedData = request.get_json()

        username = postedData["username"]
        password = postedData["password"]

        if not UserExist(username):
            retJson = {
                "status" : 301,
                "msg" : "Invalid Username"
            }
            return jsonify(retJson)

        hashed_pw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())

        users.insert_many({
            "Username" : username,
            "password" : hashed_pw,
            "Tokens" : 6
        })
        retJson = {
            "status": 200,
            "msg": "You've Successfully signed up to the API"
        }
        return jsonify(retJson)
    # end def


def verifyPw(username, password):
    """
    Purpose: verify the pass with username
    """
    if not UserExist(username):
        return False
    hashed_pw = users.find({
        "Username": username
    })[0]["Password"]

    if bcrypt.hashpw(password.encode('utf8', hashed_pw)) ==hashed_pw:
        return True
    else:
        return False
# end def

def countTokens(username):
    """
    Purpose: checks number of tokens a user has to use the API
    """
    tokens = users.find({
        "Username": username
    })[0]["Tokens"]
    return tokens
# end def


class Detect(Resource):
    def post(self):
        """
        Purpose: checks 2 texts similarity
        """
        postedData = request.get_json()

        username = postedData("username")
        password = postedData("password")
        text1 = postedData("text1")
        text2 = postedData("text2")

        if not UserExist(username):
            retJson = {
                "status" : 301,
                "msg" : "Invalid User"
            }
            return jsonify(retJson)
        correct_pw = verifyPw(username, password)

        if not correct_pw:
            retJson = {
                "status" : 302,
                "msg" : "Invalid Password"
            }
            return jsonify(retJson)
        num_tokens = countTokens(username)

        if num_tokens <= 0:
            retJson = {
                 "status" : 303,
                "msg" : "Refill tokens"
            }
            return jsonify(retJson)

        # calc the edit distance
        nlp = spacy.load('en_core_web_sm')

        text1 = nlp(text1)
        text2 = nlp(text2)

        #Ratio of the 2: closer to 1 they are similar closer 2 0 different

        ratio = text1.similarity(text2)

        retJson = {
             "status" : 200,
             "similarity" : ratio,
             "msg": "Similarity score calculated succesfully"
        }

        current_tokens = countTokens(username)
        users.update_many({
            "Username": username
        },{
            "$set":{
                "Tokens": current_tokens-1
            }
        })
        return jsonify(retJson)