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

model = load_model('model-1.h5')


# model = ResNet50(weigths='imagenet')
# model.save('')

@app.route('/')
def index():
    return "Mini project MedAyu. Use /class with POST method to access  this API with params:test_url "


@app.route('/class', methods=['POST'])
def classify():
    label_map = {0: 'Adhatoda Vasica',
                 1: 'Annona retisulate',
                 2: 'Barleria Prionitis Linn',
                 3: 'Bauchanania Latifolia roxd',
                 4: 'Bauhinia veriegata',
                 5: 'Bixa Orellana Linn',
                 6: 'Bryopllum pinnatum lam kurz',
                 7: 'Cassia Fistula',
                 8: 'Celastrus Paniculatus Wild',
                 9: 'Citrus Acida Pers',
                 10: 'Clerodendrum Infortunatum',
                 11: 'Commiphora Mukul',
                 12: 'Eaginia Jambolana',
                 13: 'Emblica officinalis',
                 14: 'Erythina variegata',
                 15: 'Ficus hispida linn',
                 16: 'Gardenia Gummifera LF',
                 17: 'Gommiphora mukul',
                 18: 'Ichnocarpus fruitescens',
                 19: 'Manikara hexandra',
                 20: 'Morinda Citrifolia Linn',
                 21: 'Paederia foetida Linn',
                 22: 'Premna IntigriFolia Linn',
                 23: 'Rasa Centifolia Linn',
                 24: 'S. Cheleonidis',
                 25: 'Salmaila Malabarica',
                 26: 'Sapindus Trifoliatus Linn',
                 27: 'Saraca Asoka',
                 28: 'Tamarindus indica',
                 29: 'Terminalia Bellirica Roxb',
                 30: 'Terminalia chebula retz',
                 31: 'Vitex Negundo',
                 32: 'Weddallia calendulaceae',
                 33: 'Withania Somnifera Linn',
                 34: 'Woodfordia Fructicose'}

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
