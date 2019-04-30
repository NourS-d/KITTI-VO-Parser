import numpy as np
import yaml

sequence = "00" # Sequence Number
directory = "/home/user/Data/data_odometry_gray/dataset/" # Change to your directory



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

def getCalibrationMatrix(num=0):
    """ 
    Parses the Calibration Matrix from the provided dataset file
    Change 'num' to select projection matrix. Be careful to remove the [:3,:3]
    in the return if you want to use it
    """
    
    calib = folder + "sequences/"+sequence+"/calib.txt"

    f= open(calib)
    Ks = yaml.safe_load(f)
    f.close()

    key = "P"+str(num)
    
    if key in Ks:
        txt = Ks[key]
        return np.fromstring(txt, dtype=float, sep=" ").reshape((3,4))[:3,:3]
    else:
        print("\n*** Error reading calibration matrix ***")


