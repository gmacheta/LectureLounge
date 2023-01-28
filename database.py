from pymongo import MongoClient

class DB_Client:

    def __init__(self):
        
        try:
    
            self.CONNECTION_STRING = "mongodb+srv://<user>:<SpartaHack8>@spartahack8.jdqhm8z.mongodb.net/?retryWrites=true&w=majority"
            
            self.client = MongoClient(self.CONNECTION_STRING)
            
            print("It connected")
        
        except:
            
            print("Did not connect")

dbname = DB_Client()

print(dbname)