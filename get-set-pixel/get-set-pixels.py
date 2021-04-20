# USAGE
# python opencv_getting_setting.py

# import necessary packages
import argparse
import cv2

# construct the argument parser and parse the argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="hitchhikers.jpg", # you can set your own --image value in the argument
                help="path to the input image")
args = vars(ap.parse_args())

# load the image and grab spatial dimensions
image = cv2.imread(args["image"]) # pass in path to input image, load input image from disk
(h, w) = image.shape[:2] # every image converted to numpy array has a shape HxWxC, return just H and W
# h = image.shape[0]
# w = image.shape[1]
# remember w=600 x h=400 inverse from # of rows then # of columns
cv2.imshow("Original", image) # display image to screen

# images are just NumPy arrays with origin at [0,0] located at the top-left
# access pixel in BGR instead of RGB ordering, because 20 years ago BGR was the std.
# if you switch ordering now, will break every app developed over last 20 years
(b, g, r) = image[0, 0]
print("Pixel at (0, 0 - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# check another pixel at height x=20, width y=50
# REMEMBER (y, x) ordering (LEFT/RIGHT, UP/DOWN)
(b, g, r) = image[50, 20]
print("Pixel at (0, 0 - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# update the pixel at (50, 20) and set to red
# remember x=5 and y=20
image[50, 20] = (0, 0, 255) # update the pixel value
(b, g, r) = image[50, 20] # print out the pixel value to verify update
print("Pixel at (50, 20) = Red: {}, Green: {}, Blue {}".format(r, g, b))

# compute the center of the image, which is simply the width / 2, height / 2
(cX, cY) = (w // 2, h // 2)

# similarly, crop the top-right, bottom-right, bottom -eft
tl = image[0:cY, 0:cX] # origin 0: rows vertical, origin 0, rows horizontal
cv2.imshow("Top-Left Corner", tl)

# Apply NumPy array slicing to grab large chunks /regions of interest from the image
# grab the top-left corner of the image
# NumPy Syntax is image[startY:endY, startX: endX]
tr = image[0:cY, cX:w] # top-left array slice
br = image[cY:h, cX:w] # bottom-right array slice
bl = image[cY:h, 0:cX] # bottom-left array slice
cv2.imshow("Top-Right Corner", tr)
cv2.imshow("Bottom-Right Corner", br)
cv2.imshow("Bottom-Left Corner", bl)

# set the top-left corner of the original image to green
image[0:cY, 0:cX] = (0, 255, 0)  # in BGR order

# show our updated image
cv2. imshow("Updated", image)
cv2.waitKey(0)

# source: https://www.pyimagesearch.com/2021/01/20/opencv-getting-and-setting-pixels/