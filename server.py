from flask import Flask, request
from flask_cors import CORS, cross_origin
import pymongo
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Mongo docker container IP
#IP = "db"
#PORT = 27017

IP = "localhost"
PORT = 27017

app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

print("server.py defining endpoint")
@app.route("/endpoint", methods=['POST'])
@cross_origin()
def endpoint():
    
    print("Endpoint reached.")
    req_dict = request.get_json()

    try:
        database = CallDatabase(IP, PORT, "/app")
        database.connect()
        print("Connected to database")
        print("QQQQQ Starting data query")
        #id = database.store_data("character_name", req_dict["name"])
        #id2 = database.store_data("character_level", req_dict["level"])
        id = database.store_data(req_dict)
        print("Finishing data query here")
        print(id)
        all_contents = database.log_all_data()
        database.disconnect()
        print("Disconnected from database")
    except:
        print("Couldn't connect to database")

    print("responding to request")
    return '{ "_id": "' + str(id) + '", "db_contents": "' + str(all_contents) + '" }'
    #return '{ "_id": "1234567890" }'

class CallDatabase:

    def __init__(self, host, port, db_name):
        self.host = host
        self.port = port
        self.db_name = db_name

    def connect(self):
        print("connecting to database")
        self.client = MongoClient(self.host, self.port)
        self.check_connection()
        self.db = self.client.app
        print(self.db)

    def check_connection(self):
        try:
            # Blocks until connection established
            self.client.admin.command('ping')
            print("Database avaliable")
        except ConnectionFailure:
            print("Database not avaliable")

    #def store_data(self, key, value):
    def store_data(self, req_dict):
        new_cl = self.db["character_sheets"]
        try:
            result = new_cl.insert_one({
                "character_name": req_dict["name"],
                "character_level": req_dict["level"]
            })
            return result.inserted_id
            #name = [{"character_name": req_dict["name"]}]
            #insert_list = [{"character_name": req_dict["name"], "character_level": req_dict["level"]}]
            #result = new_cl.insert_many(insert_list)
            #result = new_cl.insert_one(name)
            #return result.inserted_ids
        except Exception as e:
            print(e)
            print("Failed to add data to the collection.")
        return -1

    def log_all_data(self):
        new_cl = self.db["character_sheets"]
        try:
            results = []
            for result in new_cl.find():
                results.append(result)
                print(result)
                print(type(result))
            return str(results)



            # results = new_cl.find()
            # print(results)
            # print(type(results))
            # return str(results)
        except Exception as e:
            print(e)
            print("Failed to find data from the collection.")
        return -1

    def disconnect(self):
        self.client.close()
