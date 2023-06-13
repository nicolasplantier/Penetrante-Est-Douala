import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image
import os
import scipy.signal as sps
from scipy import ndimage

""" 
We will now try and compare the fft of multiple images from the PST. 
"""

# ------------------------------------------------------------------------------------------------------------------
# FIRST We download big image and the little patch representing the PST
# ------------------------------------------------------------------------------------------------------------------


current_path = os.getcwd()
path_to_im = os.path.join(current_path, "DJI_0480.JPG")
im = Image.open(path_to_im)
array_im = np.asarray(im) #That is the first orginale Image

path_to_patch = os.path.join(current_path, "test_patch_PST.JPG")
im_PST = ndimage.imread(path_to_patch, flatten = True)
array_im_PST = np.asarray(im_PST)  #That is the small image (100x100) where we only have the PST 



# ------------------------------------------------------------------------------------------------------------------
# SECOND we try to obtain the fft of this image 
# ------------------------------------------------------------------------------------------------------------------

