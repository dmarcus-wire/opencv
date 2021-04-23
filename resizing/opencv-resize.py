# USAGE
# pytyhon opencv-resize.py

# import necessary packages
import argparse # cli
import imutils # image process routines, encapsulates opencv
import cv2 # pure opencv

# construct argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image", type=str, default="profile.jpg",
                help="path to input image")
args = vars(ap.parse_args())

# load image from disk and display
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# resize image to 150 pixels
# use aspect ratio to avoid distortion
r = 150.0 / image.shape[1] # new width / old width = ratio (r)
dim = (150, int(image.shape[0] * r)) #  width of 150, h x r = aspect ratio

resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized)

# resize image to width of 50 pixels keeping aspect ratio
r = 50.0 / image.shape[0] # new height 50 pix tall / orig heigth = aspect ration
dim = (int(image.shape[1] * r), 50) # width * r, 50 px tall

# perform resize with opencv
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
cv2.waitKey(0)

# using the imutils resize function
resized = imutils.resize(image, width=100)
cv2.imshow("Resized using imutils", resized)
cv2.waitKey(0)

# what is interpolation?
# decides what pixels are kept or collapsed
# large to small is easier remove pixels, than small to large to create pixels
# rule, cv2.INTER_CUBIC/LANCZOS4 for small to large
# rule, cv2.INTER_NEAREST/LINEAR/AREA for large to small (fastest)
# list of interpolation methods in opencv
methods = [
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST), # worst method, nearest neighbor, examining nearest pixels, which is closest and keeps value
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC), # best method
    ("cv2.INTER_LANCZOS4)", cv2.INTER_LANCZOS4)] # best method, also cubic interpolation which larger dataset

# loop over the interpolation methods
for (name, method) in methods:
    # increase the size of image 3x using above methods
    print("[INFO] {}".format(name))
    resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
    cv2.imshow("Method: {}".format(name), resized)
    cv2.waitKey(0)