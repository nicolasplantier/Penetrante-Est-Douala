import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image
import os
import scipy.signal as sps

# ------------------------------------------------------------------------------------------------------------------
# FIRST We download one image to see what we can do just looking at the data like this 
# ------------------------------------------------------------------------------------------------------------------


current_path = os.getcwd()
path_to_im = os.path.join(current_path, "DJI_0480.JPG")
im = Image.open(path_to_im)
array_im = np.asarray(im) #That is the first orginale Image

path_to_patch = os.path.join(current_path, "test_patch_PST.JPG")
im_PST = Image.open(path_to_patch)
array_im_PST = np.asarray(im_PST)  #That is the small image (100x100) where we only have the PST 



# ------------------------------------------------------------------------------------------------------------------
# SECOND We first try just to see if in terms of colors we can do something 
# ------------------------------------------------------------------------------------------------------------------


# On récupère le pixel moyen 
med_pix = np.array([np.mean(array_im_PST[:,:,0]).astype(np.int64), 
                    np.mean(array_im_PST[:,:,1]).astype(np.int64), 
                    np.mean(array_im_PST[:,:,2]).astype(np.int64)])
med_image = np.ones(array_im_PST.shape)
med_image_red = med_pix[0]*np.ones((med_image.shape[0],med_image.shape[0]))
med_image_green = med_pix[1]*np.ones((med_image.shape[0],med_image.shape[0]))
med_image_blue = med_pix[2]*np.ones((med_image.shape[0],med_image.shape[0]))
med_image[:,:,0] = med_image_red
med_image[:,:,1] = med_image_green
med_image[:,:,2] = med_image_blue
med_image = med_image.astype(np.int64)



convolution1 = sps.fftconvolve(in1 = array_im[:,:,0], in2 = med_image[:,:,0], mode = 'same')
convolution2 = sps.fftconvolve(in1 = array_im[:,:,1], in2 = med_image[:,:,1], mode = 'same')
convolution3 = sps.fftconvolve(in1 = array_im[:,:,2], in2 = med_image[:,:,2], mode = 'same')
""" convolution = np.zeros((convolution1.shape[0], convolution1.shape[1], 3)).astype(np.int64)
convolution[:,:,0] = convolution1
convolution[:,:,1] = convolution2
convolution[:,:,2] = convolution3  """
convolution = convolution1 + convolution2 + convolution3
""" convolution = sps.convolve(in1= array_im, 
                           in2 = med_image, 
                           mode = "same",
                           method = "auto") """
max = np.max(convolution)
convolution = convolution/max #That is the final convolution. You can just see it with imshow to see how it looks like. 




# ------------------------------------------------------------------------------------------------------------------
# SECOND
# ------------------------------------------------------------------------------------------------------------------