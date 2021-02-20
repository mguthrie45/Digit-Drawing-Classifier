import tensorflow as tf
import pickle
from train import *

class Model:
    input_shape = (784,)
    def __init__(self):
        self.model = None
        try:
            self.load()
        except OSError:
            self.init_model()
            self.train()
            self.save()

    def init_model(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Dense(512, input_shape=self.input_shape, activation='relu'),
            tf.keras.layers.Dense(512, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
        ])
        self.model.compile(loss='categorical_crossentropy',
                           optimizer='adam',
                           metrics=['accuracy'])

    def save(self):
        self.model.save('modelmain.wb')

    def load(self):
        self.model = tf.keras.models.load_model('modelmain.wb')

    def train(self):
        train(self)

    def predict(self, input_data: np.ndarray) -> np.ndarray:
        prediction = self.model.predict(input_data)[0]
        return prediction

    def get_most_likely(self, input_data: np.ndarray) -> int:
        prediction = self.predict(input_data)
        max_i = None
        max_p = 0
        for i in range(len(prediction)):
            if prediction[i] > max_p:
                max_p = prediction[i]
                max_i = i
        return max_i


if __name__ == '__main__':
    m = Model()