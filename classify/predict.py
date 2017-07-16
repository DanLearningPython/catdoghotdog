import cv2                 
import numpy as np         
import os                 
from random import shuffle   
import tensorflow as tf
import tflearn
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.estimator import regression
import logging

np.set_printoptions(suppress=True)
#logging.basicConfig(filename='general.log',level=logging.DEBUG)

class CatDogHotDog:

    IMG_SIZE = 50


    def process_test_data(self,path):
        
        testing_data = []
        img_num = path.split('.')[0]
        img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img, (self.IMG_SIZE,self.IMG_SIZE))
        testing_data.append([np.array(img), img_num])

        shuffle(testing_data)
        return testing_data

    def run_prediction(self,predict_image):

        LR = 1e-3

        logging.info(predict_image)

        MODEL_NAME = 'dogsvscatsvshotdogs-{}-{}.model'.format(LR, '2conv-basic')

        convnet = input_data(shape=[None, self.IMG_SIZE, self.IMG_SIZE, 1], name='input')

        convnet = conv_2d(convnet, 32, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)

        convnet = conv_2d(convnet, 64, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)

        convnet = conv_2d(convnet, 128, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)

        convnet = conv_2d(convnet, 64, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)

        convnet = conv_2d(convnet, 32, 5, activation='relu')
        convnet = max_pool_2d(convnet, 5)

        convnet = fully_connected(convnet, 1024, activation='relu')
        convnet = dropout(convnet, 0.8)

        convnet = fully_connected(convnet, 3, activation='softmax')
        convnet = regression(convnet, optimizer='adam', learning_rate=LR, loss='categorical_crossentropy', name='targets')

        model = tflearn.DNN(convnet, tensorboard_dir='log')

        model.load(MODEL_NAME)

        testing_data = []
        path = '56.jpg'
        img_num = 1;

        testing_data = self.process_test_data(predict_image)
        predictions = [];

        for num,data in enumerate(testing_data):
            #dog = [0,1,0], cat = [1,0,0], hotdog = [0,0,1]
            img_num = data[1]
            img_data = data[0]
            orig = img_data
            data = img_data.reshape(self.IMG_SIZE,self.IMG_SIZE,1)
            model_out = model.predict([data])[0]
            predictions.insert(num, model_out)

                
        if np.argmax(model_out) == 1: str_label='dog'
        elif np.argmax(model_out) == 0: str_label='cat'
        else: str_label='hotdog'

        logging.info(predictions)
        
        response = {}
        response['label'] = str_label
        response['weights'] = {}
        response['weights']['cat'] = str(predictions[0][0])
        response['weights']['dog'] = str(predictions[0][1])
        response['weights']['hotdog'] = str(predictions[0][2])

        logging.info(response)

        return response
