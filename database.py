from pymongo import MongoClient
import bcrypt
import random

class DB_Client:
    def __init__(self):
        try:
            self.CONNECTION_STRING = "taken out"
            self.client = MongoClient(self.CONNECTION_STRING)
            print("It connected")
        except:
            print("Did not connect")

    def get_users_collection(self):
        return self.client["LectureLounge"]["users"]

    def get_categories_collection(self):
        return self.client["LectureLounge"]["categories"]

    def create_user(self, email, password):
        collection = self.get_users_collection()

        # Hash the password
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create the user document
        new_user = {
            "_id": email,
            "password": hashed_password
        }

        # Insert the user into the collection
        collection.insert_one(new_user)
        print("user created")

    def list_users(self):
        db_pointer = self.get_users_collection()
        for item in db_pointer.find():
            print(item)

    def list_user_categories(self, username):
        user = self.get_users_collection().find_one({"_id":username})
        return user["categories"]
    
    def post_category_post(self, category, content, date):
        
        collection = self.get_categories_collection()
        
        collection.update_one(
            {"_id":category},
            {'$push':{"post": (content, date)}}
        )
        
        
    def get_random_category_post(self):
        
        collection = self.get_categories_collection()
        
        length = collection.count_documents({})
        
        randomIndex = random.randint(1, length) - 1
        
        names = [names['_id'] for names in collection.find({}, {"_id": 1})]
        
        randomPost = [i["post"][0] for i in collection.find({"_id":names[randomIndex]}, {"_id":0})]
        
        return randomPost[0]
            
