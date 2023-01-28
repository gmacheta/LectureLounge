from pymongo import MongoClient

def get_database():
    
    CONNECTION_STRING = "mongodb+srv://<user>:<SpartaHack8>@spartahack8.jdqhm8z.mongodb.net/?retryWrites=true&w=majority"
    
    client = MongoClient(CONNECTION_STRING)
    
    return client['LectureLounge']

dbname = get_database()