
import pymongo
from flask import Flask, render_template, request, jsonify, make_response, json, send_from_directory, redirect, url_for
import pika
import logging
import warnings

# packages for swagger
from flasgger import Swagger
from flasgger import swag_from

# setup flask app
app = Flask(__name__)

# setup swagger online document
swagger = Swagger(app)

# setup logger
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning) 

# create user restful API
@app.route('/list_user', methods=['GET'])
@app.route('/', methods=['GET'])
@swag_from('apidocs/api_list_user.yml')
def create_user():

    # reture requests
    myclient = pymongo.MongoClient('mongodb://%s:%s/' % (
        'rs1',    # database addr
        '27041'         # database port
    ))
    mydb = myclient["UserList"]
    mycol = mydb["User"]
    
    x = mycol.find()
    if x:
      return render_template('home.html',data = x)
    else:
      return 'not found'


@app.route('/')
def index():
    return 'Web App with Python Flask!'


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5001)
