from PIL import Image, ImageOps
from cache_creation import cache_creation

class augment:

#flip the image upside down
    def flip(type, scale):
    
        #retrieving the cache's for the LR and HR images
        HR, LR = cache_creation.cache_method(type, scale)
        
        #the dataset is of type train
        if(type == "train"):
            for x in range(0, 799):
                #formatting the current number to use in the file path for the new image
                num = '%04d' % (x + 1)
                
                #flipping and saving the HR version of the image
                img = Image.open(HR[x])
                flipped = ImageOps.flip(img)
                filename = '../DIV2K/Augment/Train_HR_F/' + num + 'x' + str(scale) + '.png'
                flipped.save(filename, quality=95)
                
                #flipping and saving the LR version of the image
                img = Image.open(LR[x])
                flipped = ImageOps.flip(img)
                filename = '../DIV2K/Augment/Train_LR_F/' + num + 'x' + str(scale) + '.png'
                flipped.save(filename, quality=95)
        #the dataset is of type valid
        else:
            for x in range(0, 100):
                #formatting the current number to use in the file path for the new image
                num = '%04d' % (x + 1)
                
                #mirroring and saving the LR version of the image
                img = Image.open(HR[x])
                flipped = ImageOps.flip(img)
                filename = '../DIV2K/Augment/Valid_HR_F/' +  num + 'x' + str(scale) + '.png'
                flipped.save(filename, quality=95)

                #mirroring and saving the LR version of the image
                img = Image.open(LR[x])
                flipped = ImageOps.flip(img)
                filename = '../DIV2K/Augment/Valid_LR_F/' +  num + 'x' + str(scale) + '.png'
                flipped.save(filename, quality=95)
            
#mirror the image
    def mirror_image(type,scale):
        
        #retrieving the cache's for the LR and HR images
        HR, LR = cache_creation.cache_method(type, scale)
        
        #the dataset is of type train
        if(type == "train"):
            for x in range(0, 799):
                #formatting the current number to use in the file path for the new image
                num = '%04d' % (x + 1)
                
                #mirroring and saving the LR version of the image
                img = Image.open(HR[x])
                mirrored = ImageOps.mirror(img)
                filename = '../DIV2K/Augment/Train_HR_M/' + num + 'x' + str(scale) + '.png'
                mirrored.save(filename, quality=95)
                
                #mirroring and saving the LR version of the image
                img = Image.open(LR[x])
                mirrored = ImageOps.mirror(img)
                filename = '../DIV2K/Augment/Train_LR_M/' + num + 'x' + str(scale) + '.png'
                mirrored.save(filename, quality=95)
        #the dataset is of type valid
        else:
            for x in range(0, 100):
                #formatting the current number to use in the file path for the new image
                num = '%04d' % (x + 1)

                #mirroring and saving the LR version of the image
                img = Image.open(HR[x])
                mirrored = ImageOps.mirror(img)
                filename = '../DIV2K/Augment/Valid_HR_M/' +  num + 'x' + str(scale) + '.png'
                mirrored.save(filename, quality=95)

                #mirroring and saving the LR version of the image
                img = Image.open(LR[x])
                mirrored = ImageOps.mirror(img)
                filename = '../DIV2K/Augment/Valid_LR_M/' +  num + 'x' + str(scale) + '.png'
                mirrored.save(filename, quality=95)

#calling the methods to create and save the images to DIV2K
augment.mirror_image('train', 2)
augment.mirror_image('valid', 2)
augment.flip('train', 2)
augment.flip('valid', 2)

