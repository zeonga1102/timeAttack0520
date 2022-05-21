from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import numpy as np

import datetime

from pymongo import MongoClient

model = tf.keras.models.load_model('./static/model.h5')

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/api/upload', methods=['POST'])
def upload():
   file = request.files['file_give']
   fileName = request.form['title_give']
   extension = file.filename.split('.')[-1]

   timestamp = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S%f')

   path = './static/img/' + fileName + '_' + timestamp + extension
   file.save(path)

   doc = {'path': path,
          'name': fileName}

   db.images.insert_one(doc)

   return jsonify({'msg': 'success'})


@app.route('/api/search', methods=['POST'])
def search():
   fileName = request.form['name_give']

   images = list(db.images.find({'name': fileName}, {'_id': False}))

   for image in images:
      predictImg = tf.keras.preprocessing.image.load_img(image['path'], target_size=(256, 256))
      input_arr = tf.keras.preprocessing.image.img_to_array(predictImg)
      input_arr = np.array([input_arr])
      predictions = model.predict(input_arr)
      if predictions[0][0] > 0.5:
         result = '강아지'
      else:
         result = '고양이'

      image['pred'] = result

   return jsonify({'images': images})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)