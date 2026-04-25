import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

#insira seu código aqui
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0
