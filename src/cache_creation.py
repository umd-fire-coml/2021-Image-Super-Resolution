#code to create a cache for the dataset to be used in the data generator
class cache_creation:
  def cache_method(type, scale):

    train_HR_cache = []
    train_LR_cache = []

    valid_HR_cache = []
    valid_LR_cache = []

    if(type == "train"):
      for x in range(1, 800):
        num = '%04d' % x
        train_HR_cache.append('src/DIV2K/DIV2K_train_HR/' + num + '.png')

        if(scale != 8):
          scale = str(scale)
          train_LR_cache.append('src/DIV2K/DIV2K_train_LR_bicubic/X' + scale + '/' + num + 'x' + scale + '.png')
        else:
          train_LR_cache.append('src/DIV2K/DIV2K_train_LR_x8/' + num + 'x8.png')
    else:
        for x in range(801, 901):
          num = '%04d' % x
          valid_HR_cache.append('src/DIV2K/DIV2K_valid_HR/' + num + '.png')
          if(scale != 8):
            scale = str(scale)
            valid_LR_cache.append('src/DIV2K/DIV2K_valid_LR_bicubic/X' + scale + '/' + num + 'x' + scale + '.png')
          else:
            valid_LR_cache.append('src/DIV2K/DIV2K_valid_LR_x8/' + num + 'x8.png')
            
cache_creation.cache_method("train", 2)
