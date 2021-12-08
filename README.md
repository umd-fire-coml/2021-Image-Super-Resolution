# 2021-Image-Super-Resolution #

## Model Explanation ##
![example of ESPCN network](https://www.researchgate.net/profile/Laure-Tougne/publication/348205251/figure/fig3/AS:998108766953472@1614979082518/Ecient-sub-pixel-convolutional-neural-network-ESPCN-29.ppm)
1. We take a low resolution image as input.

2. The image passes through a series of layers that extract features from the image.

3. At the very end, the image with its extracted features is put into a special function called depth to space, which turns all those features into actual pixles. 

4. After this, we have our super-resolved image.

# 2021-Image-Super-Resolution #
 
## Model Explanation ##
![example of ESPCN network](https://www.researchgate.net/profile/Laure-Tougne/publication/348205251/figure/fig3/AS:998108766953472@1614979082518/Ecient-sub-pixel-convolutional-neural-network-ESPCN-29.ppm)
1. We take a low resolution image as input.
 
2. The image passes through a series of layers that extract features from the image.
 
3. At the very end, the image with its extracted features is put into a special function called depth to space, which turns all those features into actual pixles.
 
4. After this, we have our super-resolved image.
 
## DIV2K Dataset ##
We use the DIV2K dataset as our image dataset to train and test our model. The reason we choose DIV2K as our dataset is that DIV2K supports different scales of the images for training and it has high resolution (HR) images that can be used to compare with our output super-resolved (SR) images.

## Demonstrational Video: ##
[![demonstration](https://youtu.be/OMfTSoxE3QY.jpg)](https://youtu.be/OMfTSoxE3QY "T1 Super Resolution Image Demonstration")

## Google Colab: ##
[https://colab.research.google.com/drive/1sxYCYOPGuRwB46FtIq5Me8TIfXYLrpjq?usp=sharing](https://colab.research.google.com/drive/1sxYCYOPGuRwB46FtIq5Me8TIfXYLrpjq?usp=sharing)

## Description of Each File: ##
### src: ###

augment.py:

backbone.py: Defines and creates the model

cache_creation.py: Creates different caches for the data generator to use

downloader.py: Script to download the DIV2K Dataset and organize the images

generator.py: Uses the cache to generate batches of HR and LR images

test.py: Script to test the trained model and display the results

train.py: trains the model from the training dataset and saves the weights at src/x[scale]bs[batch_size]epochs[epochs]weights.h5

x2bs8epochs100weights.h5: saved weights from training the model for 100 epochs

## Citations: ##
E. Byeon, “How to download & unzip zip files in Python,” Medium, 27-Dec-2020. [Online]. Available: https://stereopickle.medium.com/how-to-download-unzip-zip-files-in-python-5f326bb1a829. [Accessed: 06-Dec-2021].
K. Team, “Keras documentation: Image Super-Resolution using an efficient sub-pixel CNN,” Keras. [Online]. Available: https://keras.io/examples/vision/super_resolution_sub_pixel/. [Accessed: 06-Dec-2021].
Roman Podlinov, John Zwinck, x-yuri, danodonovan, Ben Moskovitch, user14475672, and r1v3n, “Download large file in python with requests,” Stack Overflow, 01-Jul-1961. [Online]. Available: https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests. [Accessed: 06-Dec-2021]. 
