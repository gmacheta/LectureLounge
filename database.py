from pymongo import MongoClient
import bcrypt

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
<<<<<<< HEAD

    def create_user(self, email, password,{school}{date}{username}):
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

=======
    
>>>>>>> f9ab55d250cef186496b19583d51bbbf93903ff5
    def list_users(self):
        db_pointer = self.get_users_collection()
        for item in db_pointer.find():
            print(item)

    def list_user_categories(self, username):
        user = self.get_users_collection().find_one({"_id":username})
        return user["categories"]
    
    
       
dbname = DB_Client()

<<<<<<< HEAD



=======
dbname.create_user("tim", "10-20-12", "MSU", ["art", "history"])
>>>>>>> f9ab55d250cef186496b19583d51bbbf93903ff5

