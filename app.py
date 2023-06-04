from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola! Sam.... You created a Flask app in a Docker container!'