# USAGE
# python opencv-crop.py

# loading image from disk loads as NumPy array
# restate image = NumPy array
# to crop you need to know how opencv slices
# arrays start at 0 so the numbers are not inclusive
# ratio is row:column format
# if you go :, 3 you won't get 3..youll get up to 2
#  0  1 | 2|  3  4  5
# 10 11 |12| 13 14 15
# 20 21 |22| 23 24 25
# a[:,2] would grab the column 2, 12, 22

# NumPy is a vectorized library that is very fast

# import necessary packages
import argparse
import cv2

# construct arg parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, default="avery.jpg",
                help="path to input image")
args = vars(ap.parse_args())

# load explanation image
# python
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
cv2.waitKey(0)

# face = image
# ROI = region of interest is in Y (rows),X (columns) = array
# startY:endY
# startX:endX
# inverse from X,Y coordinates
head = image[766:886,1114:1226]
cv2.imshow("Head", head)
cv2.waitKey(0)

body = image[736:900,1226:1656]
cv2.imshow("Body",body)
cv2.waitKey(0)