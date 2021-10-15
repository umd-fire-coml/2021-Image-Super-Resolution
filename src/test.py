from cache_creation import cache_creation
#Load the model
#SR test images
#   DIV2k test
#Generate PSNR, SSIM, etc.

# Do we want a total count

total_bicubic_psnr = 0.0
total_test_psnr = 0.0

def testing():
    weights_path = ""
    arr_cache = cache_creation.cache_method("valid", 2)
    HR_cache = arr_cache[0]
    LR_cache = arr.cache[1]
    
        
    #compile the model beforehand
    
    model.load_weights(weights_path)
    
    #using arr_cache, iterate over eachimage, inputting it into model.predict
    #calculate psnr and print it, print out info about the image
    #model.predict
    
    #calculating the pnsr with respect to the low-res image and predicted image
    bicubic_psnr = tf.image.psnr(lowres_img_arr, highres_img_arr, max_val=255)
    test_psnr = tf.image.psnr(predict_img_arr, highres_img_arr, max_val=255)
    
    #computing totals
    total_bicubic_psnr += bicubic_psnr
    total_test_psnr += test_psnr
    
