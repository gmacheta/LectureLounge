from website import create_app
from flask import Flask, render_template

app = create_app()

@app.route('/sign-up')
def sign_up():
    return render_template('signup.html')

if __name__ == '__main__':
    app.run(debug=True)