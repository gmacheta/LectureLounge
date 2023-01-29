var MongoClient = require('mongodb').MongoClient;

class DB_Client {
  constructor() {
    try {
      this.CONNECTION_STRING = "mongodb+srv://User:SpartaHack8@spartahack8.jdqhm8z.mongodb.net/?retryWrites=true&w=majority";
      this.client = new MongoClient(this.CONNECTION_STRING);
      console.log("It connected");
    } catch (e) {
      console.log("Did not connect");
    }
  }

  get_users_collection() {
    return this.client["LectureLounge"]["users"];
  }

  get_categories_collection() {
    return this.client["LectureLounge"].collection("categories");
  }

  create_user(email, password) {
    var collection, hashed_password, new_user;
    collection = this.get_users_collection();
    new_user = {
      "_id": email,
      "password": password
    };
    collection.insert_one(new_user);
    console.log("user created");
  }

  list_users() {
    var db_pointer;
    db_pointer = this.get_users_collection();

    for (var item, _pj_c = 0, _pj_a = db_pointer.find(), _pj_b = _pj_a.length; _pj_c < _pj_b; _pj_c += 1) {
      item = _pj_a[_pj_c];
      console.log(item);
    }
  }

  list_user_categories(username) {
    var user;
    user = this.get_users_collection().find_one({
      "_id": username
    });
    return user["categories"];
  }

  post_category_post(category, username, content, date) {
    var collection;
    collection = this.get_categories_collection();
    collection.update_one({
      "_id": category
    }, {
      "$push": {
        "post": [username, content, date]
      }
    });
  }

  get_random_category_post() {
    var collection, length, names, randomIndex, randomPost;
    collection = this.get_categories_collection();
    length = collection.count_documents({});
    randomIndex = Math.floor(Math.random() * length) - 1;

    names = function () {
      var _pj_a = [],
          _pj_b = collection.find({}, {
        "_id": 1
      });

      for (var _pj_c = 0, _pj_d = _pj_b.length; _pj_c < _pj_d; _pj_c += 1) {
        var names = _pj_b[_pj_c];

        _pj_a.push(names["_id"]);
      }

      return _pj_a;
    }.call(this);

    randomPost = function () {
      var _pj_a = [],
          _pj_b = collection.find({
        "_id": names[randomIndex]
      }, {
        "_id": 0
      });

      for (var _pj_c = 0, _pj_d = _pj_b.length; _pj_c < _pj_d; _pj_c += 1) {
        var i = _pj_b[_pj_c];

        _pj_a.push(i["post"][0]);
      }

      return _pj_a;
    }.call(this);

    return randomPost[0];
  }

}

let DB = new DB_Client;

console.log(DB.get_categories_collection());

