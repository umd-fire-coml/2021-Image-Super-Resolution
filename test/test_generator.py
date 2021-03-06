from src.generator import DataGenerator

def test_generator():
    a = DataGenerator(2, batch_size = 8, type = "train")
    
    HR = a.HR_imgs
    LR = a.LR_imgs
    assert(LR[5] == '../DIV2K/DIV2K_train_LR_bicubic/X2/0006x2.png')
    assert(HR[1] == '../DIV2K/DIV2K_train_HR/0002.png')
