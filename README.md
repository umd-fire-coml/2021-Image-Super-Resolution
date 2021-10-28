# 2021-Image-Super-Resolution #

## Model Explanation ##
1. We take a low resolution image as input.

2. The image passes through a series of layers that extract features from the image.

3. At the very end, the image with its extracted features is put into a special function called depth to space, which turns all those features into actual pixles. 

4. After this, we have our super-resolved image.
