from PIL import Image, ImageOps
from cache_creation import cache_creation

class augment:

#flip the image upside down
    def flip(type, scale):
    
        HR, LR = cache_creation.cache_method(type, scale)
        
        if(type == "train"):
            for x in range(0, 799):
                num = '%04d' % (x + 1)
                img = Image.open(HR[x])
                flipped = ImageOps.flip(img)
                filename = '../DIV2K/Augment/Train_HR_F/' + num + 'x' + str(scale) + '.png'
                flipped.save(filename, quality=95)
                img = Image.open(LR[x])
                flipped = ImageOps.flip(img)
                filename = '../DIV2K/Augment/Train_LR_F/' + num + 'x' + str(scale) + '.png'
                flipped.save(filename, quality=95)
        else:
            for x in range(0, 100):
                num = '%04d' % (x + 1)
                img = Image.open(HR[x])
                flipped = ImageOps.flip(img)
                filename = '../DIV2K/Augment/Valid_HR_F/' +  num + 'x' + str(scale) + '.png'
                flipped.save(filename, quality=95)
                img = Image.open(LR[x])
                flipped = ImageOps.flip(img)
                filename = '../DIV2K/Augment/Valid_LR_F/' +  num + 'x' + str(scale) + '.png'
                flipped.save(filename, quality=95)
            
#mirror the image
    def mirror_image(type,scale):
        
        HR, LR = cache_creation.cache_method(type, scale)
        
        if(type == "train"):
            for x in range(0, 799):
                num = '%04d' % (x + 1)
                img = Image.open(HR[x])
                mirrored = ImageOps.mirror(img)
                filename = '../DIV2K/Augment/Train_HR_M/' + num + 'x' + str(scale) + '.png'
                mirrored.save(filename, quality=95)
                img = Image.open(LR[x])
                mirrored = ImageOps.mirror(img)
                filename = '../DIV2K/Augment/Train_LR_M/' + num + 'x' + str(scale) + '.png'
                mirrored.save(filename, quality=95)
        else:
            for x in range(0, 100):
                print("doing x")
                num = '%04d' % (x + 1)
                img = Image.open(HR[x])
                mirrored = ImageOps.mirror(img)
                filename = '../DIV2K/Augment/Valid_HR_M/' +  num + 'x' + str(scale) + '.png'
                mirrored.save(filename, quality=95)
                img = Image.open(LR[x])
                mirrored = ImageOps.mirror(img)
                filename = '../DIV2K/Augment/Valid_LR_M/' +  num + 'x' + str(scale) + '.png'
                mirrored.save(filename, quality=95)

#calling the methods to create and save the images to DIV2K
augment.mirror_image('train', 2)
augment.mirror_image('valid', 2)
augment.flip('train', 2)
augment.flip('valid', 2)

