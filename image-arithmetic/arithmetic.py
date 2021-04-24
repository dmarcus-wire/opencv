# USAGE
# python arithmetic.py

# import necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",type=str,default="teton.jpg",
                help="path to the input image")
args = vars(ap.parse_args())

# think of an image as a big array of numbers
# images = NumPy arrays as unsigned 8-bit integers (uint8)
# with values ranging from [0,255] using +/- function in opencv
# values will be clipped if they fall outside the range
added = cv2.add(np.uint8([200]), np.uint8([100])) # define value of 200 + 100 as numpy array, but we max at 255
subtracted = cv2.subtract(np.uint8([50]), np.uint8([100])) # define value of 50 - 100 as numpy array, but we min at -50

# if you add 100 to all pixel values it would lighten
# if you subtract 100 it would darken
# why care? image processing routines

print("max of 255: {}".format(added))
print("min of 0: {}".format(subtracted))

# unlike opencv that clips and stops
# NumPY performs a modulas operation
# after 255 it loops back to 0 and continues to add
# below 0 back to 255 and continues down
# could introduce difficult bugs

added = np.uint8([200]) + np.uint8([100]) # value is 44 above 255
subtracted = np.uint8([50]) - np.uint8([100]) # etc.
print("wrap around: {}".format(added))
print("wrap around: {}".format(subtracted))

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# increase pixel intesity in our input image by 100
# accomplished by constructing NumPy array that has the
# same dimensions as the input image filling it by
# multiplying by 100 and adding the input image and matrix
M = np.ones(image.shape, dtype="uint8") * 100 # define a numpy of all entries 1, with same hxwxc as the input and same data type, if we multyiple by 100 its all 100s
added = cv2.add(image, M) # add it to the original image
cv2.imshow("Lighter", added)

# we can also subtract 50 from all pixels in the image
M = np.ones(image.shape, dtype="uint8") * 50 # matrix of 1's with same hxwxc and multiply by 50
subtracted = cv2.subtract(image, M) # subtract it from the original
cv2.imshow("Darker", subtracted)
cv2.waitKey(0)