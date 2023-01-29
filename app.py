from website import create_app
from flask import Flask, render_template, request, redirect, session

app = create_app()

@app.route('/sign-up')
def sign_up():
    return render_template('signup.html')

@app.route('/login')
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # check if email and password match with records in the database
        if email == "example@email.com" and password == "password":
            session["logged_in"] = True
            return redirect("/dashboard")
        else:
            return "Invalid email or password"
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)