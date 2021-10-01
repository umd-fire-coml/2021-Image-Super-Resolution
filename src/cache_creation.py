#code to create a cache for the dataset to be used in the data generator
class cache_creation:
  def cache_method(type, scale):

    HR_cache = []
    LR_cache = []

    HR_cache = []
    LR_cache = []

    if(type == "train"):
      for x in range(1, 800):
        num = '%04d' % x
        HR_cache.append('src/DIV2K/DIV2K_train_HR/' + num + '.png')

        if(scale != 8):
          scale = str(scale)
          LR_cache.append('src/DIV2K/DIV2K_train_LR_bicubic/X' + scale + '/' + num + 'x' + scale + '.png')
        else:
          LR_cache.append('src/DIV2K/DIV2K_train_LR_x8/' + num + 'x8.png')
    else:
        for x in range(801, 901):
          num = '%04d' % x
          HR_cache.append('src/DIV2K/DIV2K_valid_HR/' + num + '.png')
          if(scale != 8):
            scale = str(scale)
            LR_cache.append('src/DIV2K/DIV2K_valid_LR_bicubic/X' + scale + '/' + num + 'x' + scale + '.png')
          else:
            LR_cache.append('src/DIV2K/DIV2K_valid_LR_x8/' + num + 'x8.png')
            
    return [HR_cache, LR_cache]
