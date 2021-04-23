# USAGE
# python opencv_rotate.py

# import necessary packages
import argparse # command line arg parsing
import imutils # convience function rotate and rotate_bound
import cv2 # binding opencv

# construct argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, default="nasa-worm.png", # default logo
                help="path to the input image")
args = vars(ap.parse_args())

# load the image and display
image = cv2.imread(args["image"]) # load image from disk
cv2.imshow("Original", image)

# grab the dimensions of the image and calculate center
(h, w) = image.shape[:2] # grab h x w
(cX, cY) = (w // 2, h // 2) # compute center

# rotate image 45 degrees around the center
# what do you want to rotate around, by what parameter, what scale
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0) # 45 degrees counterclockwise, 1.0 = scale of image (you could double with 2.0 or shrink with 0.5)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated 45 Degrees", rotated)

# rotate image -90 degrees
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0) # center coordinated, 90 degree clockwise, 1.0 scale
rotated = cv2.warpAffine(image, M, (w, h)) # set rotated image
cv2.imshow("Rotated by -90 Degrees", rotated)

# rotate image by some arbitrary number rather than center
M = cv2.getRotationMatrix2D((10, 10), 45, 1.0) # rotate around x=10, y=10, 45 degrees counterclockwise
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated Arbitrary Point", rotated)

# use imutils to rotate now, collapse two lines of messsy code into single line of code
rotated = imutils.rotate(image, 180) # rotate image 180 degrees
cv2.imshow("Rotated 180 Dergrees w/imutils", rotated)

# rotate image 33 degrees counterclockwise
# MUST keep image in view
rotated = imutils.rotate_bound(image, -33) # rotate in bounds
cv2.imshow("Rotated without cropping", rotated)
cv2.waitKey(0)

# reference: https://www.pyimagesearch.com/2017/01/02/rotate-images-correctly-with-opencv-and-python/