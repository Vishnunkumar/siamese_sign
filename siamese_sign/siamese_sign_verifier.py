import tensorflow as tf
import tensorflow_hub as hub
import cv2
import os
import numpy as np

loaded_model = tf.keras.models.load_model('model.h5', custom_objects={'KerasLayer':hub.KerasLayer})

def get_images(path_1, path_2, img_size):

  img_size = 128
  img_1 = cv2.imread(path_1)[...,::-1] 
  resized_1 = cv2.resize(img_1, (img_size, img_size)) 

  r1 = np.array(resized_1) / 255
  r1.resize(1, img_size, img_size, 3)
  r1.shape

  img_2 = cv2.imread(path_2)[...,::-1] 
  resized_2 = cv2.resize(img_2, (img_size, img_size)) 

  r2 = np.array(resized_2) / 255
  r2.resize(1, img_size, img_size, 3)

  return r1, r2


def get_predictions(r1, r2):

  predictions = loaded_model.predict([r1, r2])
  return round(predictions[0][0], 0), predictions

