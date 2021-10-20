from cache_creation import cache_creation
from tensorflow.keras.preprocessing.image import load_img
import backbone

def testing(weights):
    weights_path = 'model/weights/' + weights

    model = backbone.get_model(upscale_factor=2)
    opt = tf.keras.optimizers.Adam(learning_rate=0.001)
    model.compile(optimizer=opt, loss='mse', metrics=[tf.image.psnr])
    testing_generator = DataGenerator(scale = 2,batch_size = 1, type = 'valid', n_dataset_items=100, shuffle = False)
    model.load_weights(weights_path)
    
    total_test_psnr = 0
    for i in range (801, 901):
        lr, hr = testing_generator.__getitem__i
        lr = np.squeeze(lr)
        hr = np.squeeze(hr)
        sr = model.predict(lr)
        test_psnr = tf.image.psnr(sr, hr, max_val=255)
        total_test_psnr += test_psnr
        print("Image: " + str(i) + "PSNR: " + str(test_psnr))
        
    print("Average PSNR: " + str(total_test_psnr/100))
