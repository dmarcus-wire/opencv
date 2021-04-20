# USAGE
# python load_image_opencv.py --image image.png

# import the necessary packages
import argparse # command line arguments
import cv2 # opencv bindings

# construct the argument parser and parse the args
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, # single switch image path to image on disk
                help="path to input image")
ap.add_argument("-o", "--output", required=True, # switch image path to save image on disk
                help="path to save image")
args = vars(ap.parse_args())

# load the image from disk using cv2.imread
# grab the spatial dimensions
image = cv2.imread(args["image"]) # passing the path value to input image from argument --image, it then returns the actual image
(h, w, c) = image.shape[:3] # examine the shape of the Numpy array.
# 600 x 400 is width x height
# h is x axis and provides rows
# w is y axis and provides columns
# c is channels for 2 (gray) or 3 (BGR) channels
# BRG not RGB because opencv over 20 years ago started with BGR

# display the image width, height and channels to terminal
print("width: {} pixels".format(w))
print("height: {} pixels".format(h))
print("channels: {}".format(c))

# show the image and wait for a user keypress
cv2.imshow("Hitchhiker", image) # Image is name of window and the actual image
cv2.waitKey(0) # pause until user mouse clicks on image and hits any key

# save the image back to disk (OpenCV converts the image filytype automatically
cv2.imwrite(args["output"], image)