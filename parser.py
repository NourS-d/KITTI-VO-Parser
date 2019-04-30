import numpy as np
import yaml

sequence = "00"
directory = "/home/user/Data/data_odometry_gray/dataset/"



def readImage(idx):
    """ 
    Read image of index idx from folder and return in color and grayscale.
    Suitable for monocular visual odometry.
    """
    img =  cv2.imread(folder + 'sequences/'+ sequence +'/image_0/{0:06d}.png'.format(idx))

def readImage_Stereo(idx):
    """
    Reads the left and right image of index idx from the dataset and returns them in
    both color and greyscale.
    """
    imgL  =  cv2.imread(folder + 'sequences/'+ sequence +'/image_0/{0:06d}.png'.format(idx))
    imgR  =  cv2.imread(folder + 'sequences/'+ sequence +'/image_1/{0:06d}.png'.format(idx))
    grayL =  cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    grayR =  cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    return imgL, grayL, imgR, grayR

