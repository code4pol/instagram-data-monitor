from flask import Flask
from flask import jsonify
 
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World."
 
@app.route('/actor/<actor_name>', methods=['GET'])
def actor_name(actor_name):
    return 'actor name : %s' % actor_name

@app.route('/actorjson/<actor_name>', methods=['GET'])
def actor_name_json(actor_name):
    return jsonify({'actor_name' : actor_name})

if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    app.run()