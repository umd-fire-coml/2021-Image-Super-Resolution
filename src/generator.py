from sys import maxsize
import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import Sequence
from src.cache_creation import cache_creation


class DataGenerator(Sequence):
    '''this is a random data generator, edit this data generator to read data from dataset folder and return a batch with __getitem__'''

    def __init__(self, scale, batch_size=8, type = "train", n_dataset_items=800, shuffle = False):
        self.scale = scale
        self.batch_size = batch_size
        self.n_dataset_items = n_dataset_items
        self.indexes = np.arange(self.n_dataset_items)
        self.images = cache_creation.cache_method(type, scale)
        self.LR_imgs = self.images[1]
        self.HR_imgs = self.images[0]
        self.shuffle = shuffle
        self.on_epoch_end()
        
    def __len__(self):
        """Denotes the number of batches per epoch
        :return: number of batches per epoch
        """
        return int(np.floor(self.n_dataset_items / self.batch_size))

    def __get_input(self, index):
        LR = []
        HR = []
        
        min_h_LR = maxsize
        min_w_LR = maxsize

        # store all the LR and HR images into LR array and HR array
        for i in index:
            LR_img = tf.keras.preprocessing.image.load_img(self.LR_imgs[i])
            HR_img = tf.keras.preprocessing.image.load_img(self.HR_imgs[i])
            LR_img = np.asarray(LR_img)
            HR_img = np.asarray(HR_img)

            LR.append(LR_img)
            HR.append(HR_img)

            # find the minimum height and width of the image for cropping
            min_h_LR = min(min_h_LR,LR_img.shape[0])
            min_w_LR = min(min_w_LR,LR_img.shape[1])

        min_h_HR = self.scale * min_h_LR
        min_w_HR = self.scale * min_w_LR

        # crop the images
        for i in range (0, len(LR)):
            LR[i] = self.crop_img(LR[i], min_w_LR, min_h_LR)
            HR[i] = self.crop_img(HR[i], min_w_HR, min_h_HR)
        
        LR = np.asarray(LR)
        HR = np.asarray(HR)

        return LR, HR
    

    def __getitem__(self, index):
        """Generate one batch of data
        :param index: index of the batch
        :return: x_batch and y_batch
        """
    
        # Generate indexes of the batch
        batches = self.indexes[(index) * self.batch_size : (index+1) * self.batch_size]
        
        # Generate data
        X = self.__get_input(batches)       

        # return a batch of HR and HR images 
        return X

    def crop_img(self, img, min_height, min_width):
        crop_img = img[0:min_height, 0:min_width, ...]
        return crop_img

    def on_epoch_end(self):
        """Shuffle indexes after each epoch if shuffle is True
        """
        self.indexes = np.arange(self.n_dataset_items)
        if self.shuffle == True:
          np.random.shuffle(self.indexes)