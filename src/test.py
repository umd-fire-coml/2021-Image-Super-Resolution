import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
import backbone
import generator

def testing(weights):
    weights_path = weights

    model = backbone.get_model(upscale_factor=2)
    opt = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=opt, loss='mse', metrics=[tf.image.psnr])
    testing_generator = generator.DataGenerator(scale = 2,batch_size = 1, type = 'valid', shuffle = False)
    model.load_weights(weights_path)
    
    total_test_psnr = 0
    for i in range (0, 100):
        batch = testing_generator.__getitem__(i)
        lr = batch[0]
        hr = batch[1]
        sr = model.predict(lr)
        test_psnr = tf.image.psnr(sr, hr, max_val=255)
        total_test_psnr += test_psnr
        print("Image: " + str(i) + " PSNR: " + str(test_psnr))
        
    print("Average PSNR: " + str(total_test_psnr/100))


testing('x2bs8epochs100weights.h5')
