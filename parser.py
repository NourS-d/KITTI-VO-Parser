import numpy as np
import yaml
import cv2

sequence = "00" # Sequence Number
folder = "/home/user/data_odometry_gray/dataset/" # Change to your directory


def readImage(idx):
    """ 
    Read image of index idx from folder and return in color and grayscale.
    Suitable for monocular visual odometry.
    """
    img =  cv2.imread(folder + 'sequences/'+ sequence +'/image_0/{0:06d}.png'.format(idx))
    return img, cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


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
    Parses the Calibration Matrix and other data from the provided dataset file.
    The order of data is as follows:
    ----->K, R, t, rotX, rotY, rotZ, eular 
    """
    
    calib = folder + "sequences/"+sequence+"/calib.txt"

    f= open(calib)
    Ks = yaml.safe_load(f)
    f.close()

    key = "P"+str(num)
    
    if key in Ks:
        txt = Ks[key]
        P= np.fromstring(txt, dtype=float, sep=" ").reshape((3,4))
        return cv2.decomposeProjectionMatrix(P)
        
    else:
        print("\n*** Error reading calibration matrix ***")

def getRealPoses():
    """
    Returns the ground truth transformation matrices.
    """
    pose = folder + "poses/" + sequence + ".txt"
    poses = np.genfromtxt(pose, delimiter=' ',dtype=None)
    return poses.reshape((len(poses),3,4))


def getScale(pose, idx):
    """
    When estimating the rotation and translation from the essential matrix, the 
    translation is up to a scale.
    This function returns the true scale while moving from (idx-1) to (idx).
    Poses are supplied from the getRealPoses function.
    Useful in just testing the algorithm.
    """
    x0, y0, z0 = pose[idx-1,0,-1],pose[idx-1,1,-1],pose[idx-1,2,-1]
    x1, y1, z1 = pose[idx,0,-1],pose[idx,1,-1],pose[idx,2,-1]
    scale = np.sqrt( (x0-x1)**2 + (y0-y1)**2 + (z0-z1)**2 )
    line = [x0,y0,z0,x1,y1,z1]
    return(scale,line)

