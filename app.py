from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/index')
def index():
    return render_template('index.html')


with app.test_request_context():
    print(url_for('index'))
