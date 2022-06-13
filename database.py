from mongo_connection import MongoConnection

class Database:
    
    def __init__(self, db_name):
        self.HOST = "localhost" # non-container IP
        #self.HOST = "db" # Mongo docker container IP
        self.PORT = 27017
        #self.db_name = db_name # maybe outmoded

    def connect(self):
        print("Attempting database connection")
        self.connection = MongoConnection(self.HOST, self.PORT)
        connection_stable = self.verify_connection()
        return connection_stable

    def verify_connection(self):
        try:
            self.connection.ping()
            return True
        except:
            # retry connection TODO
            return False

    def with_connection(self, action):
        connected = self.connect()
        if not connected:
            raise Exception("Failed to connect to the database.")
        result = action()
        self.disconnect()
        return result

    def store_data(self, character_sheet):
        data_entry = {
            "character_name": character_sheet["name"],
            "character_level": character_sheet["level"]
        }
        return self.connection.store_data("character_sheets", data_entry)

    def fetch_all_data(self):
        return self.connection.fetch_all_data("character_sheets")

    def disconnect(self):
        self.connection.disconnect()
        print("Disconnected from database")
