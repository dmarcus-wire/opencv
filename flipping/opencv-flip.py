# USAGE
# python opencv-flip.py

# import necessary packages
import argparse
import imutils
import cv2

# make the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, default="avery.jpg",
                help="path to the input image")
args = vars(ap.parse_args())


# load image from disk and display
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# flip image horizontally
print("[INFO] flip image horizontally")
flipped = cv2.flip(image, 1) #params= what image to flip, how to flip 1 = hor
cv2.imshow("Flipped horizontally", flipped)

# flip image vertically
print("[INFO] flip image vertically")
flipped = cv2.flip(image, 0) # flip 0 = vertically
print("Flipped vertically", flipped)

# flip image on both axes
flipped = cv2.flip(image, -1) # flip -1 = both
print("[INFO] flip image hor. and vert.")
cv2.imshow("Flipped image horizontally and vertically", flipped)
cv2.waitKey(0)

