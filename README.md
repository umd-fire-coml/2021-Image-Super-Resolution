![](https://i.imgur.com/RvJDVCC.png)
# 2021-Image-Super-Resolution #

## Changlin Jiang, Harpreet Multani, Ian Roberts, Allen Tu (Peer Mentor) ##

## Model Explanation ##
![example of ESPCN network](https://www.researchgate.net/profile/Laure-Tougne/publication/348205251/figure/fig3/AS:998108766953472@1614979082518/Ecient-sub-pixel-convolutional-neural-network-ESPCN-29.ppm)
1. We take a low resolution image as input.

 
2. The image passes through a series of layers that extract features from the image.
 
3. At the very end, the image with its extracted features is put into a special function called depth to space, which turns all those features into actual pixles.
 
4. After this, we have our super-resolved image.
 
## DIV2K Dataset ##
We use the DIV2K dataset as our image dataset to train and test our model. The reason we choose DIV2K as our dataset is that DIV2K supports different scales of the images for training and it has high resolution (HR) images that can be used to compare with our output super-resolved (SR) images.

### Demonstrational Video: ##
[!["T1 Super Resolution Image Demonstration"](https://i.imgur.com/PBJ8OuQ.png)](https://youtu.be/OMfTSoxE3QY)

Watch this short video to see our model in action in our Interactice Notebook through Google Colab. The notebook is linked below where you can take a deeper look at our model.

## Google Colab: ##

The following is a link to a google colab version of our project, where you can view some more results of our super-resolution model:

[https://colab.research.google.com/drive/1sxYCYOPGuRwB46FtIq5Me8TIfXYLrpjq?usp=sharing](https://colab.research.google.com/drive/1sxYCYOPGuRwB46FtIq5Me8TIfXYLrpjq?usp=sharing)

## Description of Each File: ##

backbone.py: Defines and creates the model

cache_creation.py: Creates different caches for the data generator to use

downloader.py: Script to download the DIV2K Dataset and organize the images

generator.py: Uses the cache to generate batches of HR and LR images

train.py: trains the model from the training dataset and saves the weights at src/x[scale]bs[batch_size]epochs[epochs]weights.h5

test.py: Script to test the trained model and display the results

Augment.py: augments the test images to allow for a larger testing dataset

x2bs8epochs100weights.h5: saved weights from training the model for 100 epochs

requirements.txt: required python libraries

test-requirements.txt: required python libraries for automated tests

## Project Setup: ##

1. Clone this repo6ysitory
2. Run pip install -r requirements.txt from this directoy in order to install the required libraries
3. Follow the directions in Downloading Dataset to retrieve the required dataset
4. Follow the steps in Traing and Testing to create and test your model.

## Downloading Dataset: ##
Navigate to the folder containing the downloader.py file and run it, (python downloader.py) on *nix operating systems. The script should then create a "DIV2K" folder in the same directory as the script and download the entire dataset into that folder. The script also organizes the files into several folders so that it is easier to navigate. In the event the connection is interrupted or the server you are downloading from crashes, you will receive an error and you’ll have to delete the "DIV2K" folder and restart the script.
## Training: ##
Run the train.py function with python train.py [model] [scale] [batch_size] [epochs]. “model” would be the function get_model from backbone.py; “scale” is the scale the images will be super-resolved with; “batch_size” is the number of batches generated by the generator; “epochs” is the number of epochs will be trained. And then use the training.ipynb script to train the model in a Jupyter Notebook, the weight will be saved at src/x[scale]bs[batch_size]epochs[epochs]weights.h5.
## Testing: ##
Run the test.py file to test your model. In the file you have a method called testing. Call the method using the file path to the saved weights of your model. Run ‘python test.py’ in your command line. The file will run and test 100 images through your model. You will see the image number and psnr of each image printed. And finally the average psnr number of your model will be calculated and displayed. The PSNR (Peak signal-to-noise ratio) number is the ratio between the maximum possible power of a signal and the power of corrupting noise. The higher the PSNR number, the better the quality of our reconstructed image. 

## Results: ##
Example Images:

Here is a sample output of our model. On the left is the low-resolution image that we gave our model. In the middle is an high-resolution image we are trying to get our model to output. And lastly, we have the super-resolved image that our model outputs.

![final_img](https://i.imgur.com/KQta1N4.png)

We tested our model against 100 test images from the DIV2K dataset. Our model reached an average psnr of 25.28.

## Citations: ##
E. Byeon, “How to download & unzip zip files in Python,” Medium, 27-Dec-2020. [Online]. Available: https://stereopickle.medium.com/how-to-download-unzip-zip-files-in-python-5f326bb1a829. [Accessed: 06-Dec-2021].

K. Team, “Keras documentation: Image Super-Resolution using an efficient sub-pixel CNN,” Keras. [Online]. Available: https://keras.io/examples/vision/super_resolution_sub_pixel/. [Accessed: 06-Dec-2021].

Roman Podlinov, John Zwinck, x-yuri, danodonovan, Ben Moskovitch, user14475672, and r1v3n, “Download large file in python with requests,” Stack Overflow, 01-Jul-1961. [Online]. Available: https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests. [Accessed: 06-Dec-2021]. 
