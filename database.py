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
            
    def create_user(self, name, date, school, categories):
        
        collection = self.get_users_collection()
        
        new_user = {
            "_id": name,
            "date_created":date,
            "school":school,
            "categories": categories
        }
        
        collection.insert_one(new_user)
    
    def list_user_categories(self, username):
        
        user = self.get_users_collection().find({"_id":username})
        
        for cat in user.find("categories"):
            print(cat)
        
        
            
    

dbname = DB_Client()

#dbname.create_user("Jay", "10-20-12", "MSU", ["art", "history"])

dbname.list_user_categories("Jay")

