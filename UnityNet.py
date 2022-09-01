from flask import Flask, jsonify, request
from keras.models import load_model, Model
import tensorflow as tf
from PIL import Image
import numpy as np
import total_test

app=Flask(__name__)


target_names = ['Anger','Fear','Happy','Sad','Surprise']
model = load_model('.\\model_final_weight\\model_final.h5')
load_path='.\\test_data\\02.jpg'

@app.route("/")
def index():
    return jsonify(200)

@app.route("/chatbot", methods=['POST'])
def chatbot():
    chat = request.form.get('chat')
    chatAns = total_test.sinario(chat)
    print(chatAns)
    return chatAns

@app.route("/faceExpression")
def faceExpression():
    img = Image.open(load_path)
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    pred = model.predict(x)
    print(pred)
    return target_names[target_names == pred.max()]

if __name__=="__main__":
    app.run(host="localhost", port=7700)
