from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoConnection:
    
    def __init__(self, host, port):
        self.client = MongoClient(host, port)
        self.db = self.client.app

    def ping(self):
        try:
            self.client.admin.command('ping')
        except Exception as e:
            raise Exception("Ping unsuccessful")

    # returns id of inserted document, -1 if failure
    # return is unused. necessary for future feature
    def store_data(self, collection_name, document):
        collection = self.db[collection_name]
        try:
            result = collection.insert_one(document)
            print("Data stored with id: " + str(result.inserted_id))
            return str(result.inserted_id)
        except Exception as e:
            print(e)
            print("Failed to add data to the collection.")
        return -1

    # returns id of inserted document, -1 if failure
    # return is unused. necessary for future feature
    def fetch_all_data(self, collection_name):
        collection = self.db[collection_name]
        try:
            document_list = []
            for document in collection.find():
                document_list.append(document)
            return str(document_list)
        except Exception as e:
            print(e)
            print("Failed to find data from the collection.")
        return -1

    def disconnect(self):
        self.client.close()