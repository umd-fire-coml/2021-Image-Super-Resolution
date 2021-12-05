import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.image import load_img
import backbone
import generator

def testing(weights):

    #saving the file paths of the weights in a file
    weights_path = weights

    #loading the model and compiling it
    model = backbone.get_model(upscale_factor=2)
    opt = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=opt, loss='mse', metrics=[tf.image.psnr])
    testing_generator = generator.DataGenerator(scale = 2,batch_size = 1, type = 'valid', shuffle = False)
    model.load_weights(weights_path)
    
    total_test_psnr = 0
    
    #predicting images using our model and calculating the psnr for each image
    for i in range (0, 100):
        batch = testing_generator.__getitem__(i)
        img = array_to_img(np.resize(batch[1],(1356, 2040, 3)))
        lowres_input = array_to_img(np.resize(batch[0],(678, 1020, 3)))
        w = lowres_input.size[0] * upscale_factor
        h = lowres_input.size[1] * upscale_factor
        highres_img = img.resize((2040, 1356))
        prediction = array_to_img(np.resize(model.predict(batch[0]),(1356, 2040, 3)))
        highres_img_arr = img_to_array(highres_img)
        predict_img_arr = img_to_array(prediction)
        
        test_psnr = tf.image.psnr(predict_img_arr, highres_img_arr, max_val=255)
        total_test_psnr += test_psnr
        print("Image: " + str(i) + " PSNR: " + str(test_psnr))
        
    #pringint the total average PSNR for all of the images
    print("Average PSNR: " + str(total_test_psnr/100))


#calling our method on the current model's saved weights
testing('x2bs8epochs100weights.h5')
