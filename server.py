from flask import Flask, request
from flask_cors import CORS, cross_origin

from database import Database

FLASK_SERVER = Flask(__name__)
# cors must be defined for use in flask decorators
cors = CORS(FLASK_SERVER)
FLASK_SERVER.config['CORS_HEADERS'] = 'Content-Type'

@FLASK_SERVER.route("/endpoint", methods=['POST'])
@cross_origin()
def create_character():
    character_sheet = request.get_json()
    character_list = ''

    try:
        database = Database("/app")
        data_tuple = database.with_connection(lambda : (
                database.store_data(character_sheet),
                database.fetch_all_data()
            )
        )
        id, db_contents = data_tuple
        
    except:
        print("Couldn't connect to database")

    return '{ "_id": "' + id + '", "db_contents": "' + db_contents + '" }'
