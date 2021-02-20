import tensorflow as tf
import numpy as np
from keras.datasets import mnist
from keras.utils import np_utils

def get_data():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(60000, 784).astype('float32')/255
    x_test = x_test.reshape(10000, 784).astype('float32')/255
    y_test = np_utils.to_categorical(y_test, 10)
    y_train = np_utils.to_categorical(y_train, 10)
    return (x_train, y_train, x_test, y_test)

def train(model):
    x_train, y_train, x_test, y_test = get_data()
    model.model.fit(x_train, y_train,
                    batch_size=128, epochs=20,
                    verbose=2,
                    validation_data=(x_test, y_test))