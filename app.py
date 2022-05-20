from flask import Flask, render_template, request, jsonify, redirect, url_for
from werkzeug.utils import secure_filename
from bson.objectid import ObjectId

import datetime

from pymongo import MongoClient


app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload():
   file = request.files['file_give']
   fileName = request.form['title_give']

   timestamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')

   path = './static/img/' + fileName + '_' + timestamp
   file.save(path)

   return jsonify({'msg': 'success'})


# @app.route('/search')
# def search():


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)