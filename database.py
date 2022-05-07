from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class Database:
    
    def __init__(self, db_name):
        self.HOST = "localhost" # non-container IP
        #self.HOST = "db" # Mongo docker container IP
        self.PORT = 27017
        self.db_name = db_name

    def connect(self):
        print("Attempting database connection")
        self.client = MongoClient(self.HOST, self.PORT)
        self.verify_connection()
        self.db = self.client.app

    def verify_connection(self):
        try:
            self.client.admin.command('ping')
            print("Database avaliable")
        except ConnectionFailure:
            print("Database not avaliable")

    def store_data(self, character_sheet):
        character_collection = self.db["character_sheets"]
        try:
            result = character_collection.insert_one({
                "character_name": character_sheet["name"],
                "character_level": character_sheet["level"]
            })
            print("Data stored with id: " + result.inserted_id)
            return result.inserted_id
        except Exception as e:
            print(e)
            print("Failed to add data to the collection.")
        return -1

    def fetch_all_data(self):
        character_collection = self.db["character_sheets"]
        
        try:
            character_list = []
            for character_sheet in character_collection.find():
                character_list.append(character_sheet)
            return str(character_list)
        except Exception as e:
            print(e)
            print("Failed to find data from the collection.")
        return -1

    def disconnect(self):
        self.client.close()
        print("Disconnected from database")
