# USAGE
# python image_drawing.py

# import necessary packages
import argparse
import cv2

# construct the argument parse
ap = argparse.ArgumentParser()
# single switch argument with default jpg
ap.add_argument("-i", "--image", type=str, default="hitchhikers.jpg",
                help="path to the input image")
args = vars(ap.parse_args())

# load input image from disk
image = cv2.imread(args["image"])

# draw a circle around something
cv2.circle(image, (168, 188), 90, (0, 0, 255), 2)
cv2.circle(image, (150, 164), 10, (0, 0, 255), -1)
cv2.circle(image, (192, 174), 10, (0, 0, 255), -1)
cv2.rectangle(image, (134, 200), (186, 218), (0, 0, 255), -1)

# show image
cv2.imshow("Output", image)
cv2.waitKey(0)