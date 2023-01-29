from website import create_app
from database import DB_Client
from flask import request, jsonify
import datetime as date

app = create_app()

DB = DB_Client()

@app.route("/post", methods=["POST"])
def post_data():
    data = request.get_json()
    className = data["name"]
    content = data["content"]
    dateCreated = date.datetime.now()
    
    DB.post_category_post(className, content, dateCreated)

    # Perform any necessary operations with the data

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)