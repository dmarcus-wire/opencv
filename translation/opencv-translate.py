# USAGE
# python opencv_translate.py

# import necessary packages
import numpy as np # numerical processing, construct translation matrix 2 rows x 3 columns
import argparse # commandline arguments
import imutils # translate function to collapse earlier lines into a single line
import cv2 # opencv bindings

# construct arg parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, default="nasa-worm.png", # single switch image to image on disk
                help="path to the input image")
args = vars(ap.parse_args())

# load the image and display
image = cv2.imread(args["image"]) # load image from disk
cv2.imshow("Original", image) # display from screen

# NOTE: translating (shifting) an image is given by NumPy matrix
# [1, 0, shiftX],
# [0, 1, shiftY]
# you specify how many pixels you want to shift the image in the X / Y direction
# - left + right
# - up + down

# shift the image 25 pixels to the RIGHT and 50 pixels DOWN
M = np.float32([[1, 0, 15], [0, 1, 50]]) # translation matrix, 32 bit float, 2 rows 3 columns
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

# now shift image 50 pixels LEFT and 90 pixels UP
# up by negative values
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# use imutils helper function to translate the image 100 pixels
shifted = imutils.translate(image, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)