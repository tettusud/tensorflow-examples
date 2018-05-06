from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from flask import Flask,jsonify,json,request,render_template
from PIL import Image

import numpy as np
import cv2
import keras
import tensorflow as tf


app = Flask(__name__,static_url_path='') #create the Flask app

def init():   	  
	#load woeights into new model
	model=load_model("model.h5")
	print("Loaded Model from disk")
	#compile and evaluate loaded model
	model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])
	#loss,accuracy = model.evaluate(X_test,y_test)
	#print('loss:', loss)
	#print('accuracy:', accuracy)
	graph = tf.get_default_graph()
	return model,graph

model,graph = init()

@app.route('/predict', methods=['POST']) #GET requests will be blocked
def predict():
    mnist_data = 255-np.array(request.json, dtype=np.uint8)  .reshape(280,280)    
    resized=cv2.resize(mnist_data, dsize=(28, 28))
    reshaped=resized.reshape(28,28,1)
    reshaped=np.expand_dims(reshaped, axis=0)  
    with graph.as_default():
     predictions=model.predict_classes(reshaped) 
     print(predictions)
     return jsonify({"class":str(predictions[0])})
     
@app.route('/')
def root():
    return render_template('index.html')

if __name__ == '__main__':    
    app.run(debug=True, port=8080)