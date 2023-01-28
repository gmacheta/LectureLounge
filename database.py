from pymongo import MongoClient

class DB_Client:

    def __init__(self):
        
        try:
    
            self.CONNECTION_STRING = "mongodb+srv://User:SpartaHack8@spartahack8.jdqhm8z.mongodb.net/?retryWrites=true&w=majority"
            
            self.client = MongoClient(self.CONNECTION_STRING)
            
            print("It connected")
        
        except:
            
            print("Did not connect")
            
    def get_users_collection(self):
        
        return self.client["LectureLounge"]["users"]
    
    def get_categories_collection(self):
        
        return self.client["LectureLounge"]["categories"]
    
    def list_users(self):
        
        db_pointer = self.get_users_collection()
        
        for item in db_pointer.find():
            print(item)
            
    

dbname = DB_Client()

