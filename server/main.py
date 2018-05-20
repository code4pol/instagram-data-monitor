from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/actors', methods=['GET'])
def list_actors():
    with open('./json/atores.json') as data:
        json_data = ''
        for line in data:
            json_data += line
        return json_data


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)