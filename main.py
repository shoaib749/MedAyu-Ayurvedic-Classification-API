from flask import Flask, request, jsonify
from keras.models import load_model
import tensorflow as tf
import numpy as np

# import cv2
# import keras.applications.resnet50 import ResNet50
# for importing image from url
from skimage import io
# from app import app

app = Flask(__name__)

model = load_model('model.h5')


# model = ResNet50(weigths='imagenet')
# model.save('')

@app.route('/')
def index():
    return "Mini project MedAyu. Use /class with POST method to access  this API with params:test_url "


@app.route('/class', methods=['POST'])
def classify():
   


    with open("plants_name_114.txt","r") as file:
        lines = file.readlines()
    label_map ={}
    for i in range(len(lines)):
        label_map[i] = lines[i].strip()
    print(label_map)
    image_url = request.form.get('test_url')
    image_array = io.imread(image_url)
    # testing for preprocessing
    img_array = np.rint(image_array)
    img_array = img_array.astype('uint8')
    # hsv_img = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)
    # mask = cv2.inRange(hsv_img, (25, 25, 0), (95, 270, 255))
    # result = cv2.bitwise_and(img_array, img_array, mask=mask)
    # result = result.astype('float64')

    image_array = tf.image.resize(img_array, [150, 150])
    img_array = tf.expand_dims(image_array, 0)

    preds = model.predict(img_array)
    # labling based on predication
    print(preds)
    predicted_class_indices = np.argmax(preds, axis=1)
    prediction_labels = [label_map[k] for k in predicted_class_indices]
    print(prediction_labels[0])
    result = {'class': prediction_labels[0]}
    return jsonify(result)


if __name__ == '__main__':
    print("working")
    app.run(debug=True, host="0.0.0.0")
