from verify import check

def test_verify():
    assert(check(1) == "test done")
    #"Checking dataset... \n DIV2K/DIV2K_train_LR_bicubic is MISSING! DIV2K/DIV2K_train_LR_unknown is MISSING!\n DIV2K/DIV2K_valid_LR_bicubic is MISSING!\nDIV2K/DIV2K_valid_LR_unknown is MISSING!\nDIV2K/DIV2K_train_LR_x8 is MISSING!\nDIV2K/DIV2K_train_LR_mild is MISSING!\nDIV2K/DIV2K_train_LR_difficult is MISSING!\nDIV2K/DIV2K_train_LR_wild is MISSING!\nDIV2K/DIV2K_valid_LR_difficult is MISSING!\nDIV2K/DIV2K_valid_LR_wild is MISSING!\nDIV2K/DIV2K_train_HR is MISSING!\nDIV2K/DIV2K_valid_HR is MISSING!"