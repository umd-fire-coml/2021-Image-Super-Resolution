import os
from os import path

def check(verbose):
   # Check if DIV2K is a complete dataset.
   if verbose == 1:
        print('Checking dataset...')
   dataset_path = 'DIV2K'
   if path.exists(dataset_path):
       # Check if .. contains all required LR subsets.
       subsets_LR = ["DIV2K_train_LR_bicubic","DIV2K_train_LR_unknown", 
       "DIV2K_valid_LR_bicubic", "DIV2K_valid_LR_unknown"]
       for subset in subsets_LR:
           subset_path = dataset_path + '/' + subset
           if path.exists(subset_path):
               # Check if each subset contains all required scales.
               scales = ['X2', 'X3', 'X4']
               for scale in scales:
                   scale_path = subset_path + '/' + scale
                   if path.exists(scale_path) == False:
                       print(scale_path + ' is MISSING!')
           else:
               print(subset_path + ' is MISSING!')
       # Check if DIV2K contains all required HR subsets.
       subsets_HR = ["DIV2K_train_LR_x8", "DIV2K_train_LR_mild", "DIV2K_train_LR_difficult", 
       "DIV2K_train_LR_wild", "DIV2K_valid_LR_difficult", "DIV2K_valid_LR_wild", 
       "DIV2K_train_HR", "DIV2K_valid_HR"]
       for subset in subsets_HR:
           subset_path = dataset_path + '/' + subset
           if path.exists(subset_path) == False:
               print(subset_path + ' is MISSING!')
   else:
       print('DIV2K is MISSING!')


check(1)
