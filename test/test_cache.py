from src.cache_creation import cache_creation

def test_cache():
    arr = cache_creation.cache_method("train", 2)
    
    HR = arr[0]
    LR = arr[1]
    assert(LR[3] == 'src/DIV2K/DIV2K_train_LR_bicubic/X2/0004x2.png')
    assert(HR[5] == 'src/DIV2K/DIV2K_train_HR/0006.png')
