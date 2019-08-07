from flask import Flask, render_template, request, url_for, jsonify

from search.getLocation import get_location

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def getLocationList():
    result = request.form['searchInput']
    print(result)
    response_data = get_location(result)

    return render_template('search-result.html', contents=response_data)


with app.test_request_context():
    print(url_for('index'))
    print(url_for('getLocationList'))
