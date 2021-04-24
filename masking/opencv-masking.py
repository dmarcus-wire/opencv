# USAGE
# python opencv-masking.py

# import packages
import numpy as np #initial mask
import argparse
import cv2

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="profile.jpg",
                help="path to input image")
args = vars(ap.parse_args())

# load the image from disk
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# a mask is the same size as our image, but has only two pixels
# values, 0 and 255 -- pixels with a background of 0 are ignored
# while mask pizels with a value of 255 (foreground) are allowed/kept
mask = np.zeros(image.shape[:2], dtype="uint8") # allocate memory mask must have same spatial image as original, canvas mask pf 0's (background)
cv2.rectangle(mask, (0, 90), (290, 450), 255, -1) # draw rectangle on the image
cv2.imshow("Rectangular Mask", mask)

# apply the mask, notice the person is cropped
masked = cv2.bitwise_and(image, image, mask=mask) #input image with mask keyword, only the bitwise will be 0 and rest are 0
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)

# apply the circular mask with radius of 100 pixels
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.circle(mask,  (200, 160), 100, 255, -1)
masked = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Circular Mask", mask)
cv2.imshow("Mask Applied to Image", masked)
cv2.waitKey(0)