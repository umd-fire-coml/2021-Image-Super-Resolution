#code to create a cache for the dataset to be used in the data generator
class cache_creation:
  def cache_method(type, scale):

    #cache initialization
    HR_cache = []
    LR_cache = []
    
    #requested dataset is train
    if(type == "train"):
      for x in range(1, 800):
        #formatting x to match with file path
        num = '%04d' % x
        
        #adding file path to the HR cache
        HR_cache.append('../DIV2K/DIV2K_train_HR/' + num + '.png')

        #Adding to the LR cache
        
        #scale of images requested is not 8
        if(scale != 8):
          scale = str(scale)
          LR_cache.append('../DIV2K/DIV2K_train_LR_bicubic/X' + scale + '/' + num + 'x' + scale + '.png')
        #image scale requested is 8
        else:
          LR_cache.append('../DIV2K/DIV2K_train_LR_x8/' + num + 'x8.png')
    #requested dataset is valid
    else:
        for x in range(801, 901):
          #formatting x to match with file path
          num = '%04d' % x
          
          #Adding file path to the HR cache
          HR_cache.append('../DIV2K/DIV2K_valid_HR/' + num + '.png')
          
          #Adding file path to the LR cache
          
          #scale of images requested is not 8
          if(scale != 8):
            scale = str(scale)
            LR_cache.append('../DIV2K/DIV2K_valid_LR_bicubic/X' + scale + '/' + num + 'x' + scale + '.png')
         #image scale requested is 8
          else:
            LR_cache.append('../DIV2K/DIV2K_valid_LR_x8/' + num + 'x8.png')

    #returning both caches
    return [HR_cache, LR_cache]
