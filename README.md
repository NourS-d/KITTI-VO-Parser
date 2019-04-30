# KITTI-VO-Parser
A simple parser for the KITTI Dataset.
To select a sequence simply edit the sequence string in the 'parser.py' file.

#### Dependencies:
- numpy
- yaml

#### Functions:
- __*readImage(idx)*__ : takes the index of the frame and returns the corresponding image in color and grayscale
- __*readImage_Stereo (idx)*__ : takes index of the frame and returns the stereo pairs in the following order  "_image_Left, grayImage_Left, image_Right, grayImage_Right_"
- __*getCalibrationMatrix ()*__ : returns the calibration matrix.
- __*getReadlPoses()*__ : returns the ground truth poses.
