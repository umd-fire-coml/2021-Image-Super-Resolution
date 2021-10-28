# 2021-Image-Super-Resolution #

## Model Explanation ##
![example of ESPCN network](https://www.researchgate.net/profile/Laure-Tougne/publication/348205251/figure/fig3/AS:998108766953472@1614979082518/Ecient-sub-pixel-convolutional-neural-network-ESPCN-29.ppm)
1. We take a low resolution image as input.

2. The image passes through a series of layers that extract features from the image.

3. At the very end, the image with its extracted features is put into a special function called depth to space, which turns all those features into actual pixles. 

4. After this, we have our super-resolved image.
