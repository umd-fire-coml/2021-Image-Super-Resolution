import os
import tensorflow as tf
from src.backbone import get_model

def test_get_model():
	model = get_model()
	for x in range(1, len(model.layers)-1):
		assert(isinstance(model.get_layer(index=x), tf.keras.layers.Conv2D))

