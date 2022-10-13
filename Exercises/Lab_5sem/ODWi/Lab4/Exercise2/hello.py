from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def hello_world():
    return 'Welcome to this awesome page!'