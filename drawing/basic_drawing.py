# USAGE
# python basic_drawing.py

# import necessary packages
import numpy as np # using it to initialize blank canvas
import cv2

# initialize canvas as 300x300 with 3 channels
# RGB with black background
canvas = np.zeros((300,300,3), dtype="uint8") # blank empty canvas to draw on, filled with 0's, unsigned 8 byte integer

# draw a green line from the top-left corner to bottom-right
# BGR order
green = (0, 255, 0) # green tuple
cv2.line(canvas, (0, 0), (300, 300), green) # top-left 0, 0 to bottom-right 300, 300
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a 3 pixel thick red line from top-right to bottom-left
# what will you draw on, where will you start, where will you end, what color, what thickness
red = (0, 0, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3) # top-right to bottom-left
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# similar approach
# what will you draw on, where will you start, where will you end, what color, what thickness
# draw a 50x50 pixel square starting at 10x10
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw another rectangle with 5 pixel thickness
cv2.rectangle(canvas, (50, 200), (200, 255), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw a filled in rectangle simple as supplying -1 thickness
blue = (255, 0, 0)
cv2.rectangle(canvas, (200, 50), (255, 125), blue, -1) # -1 indicates filled in
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# draw circles
# re-initialize canvas so it's empty
# compute center at (x, y) of canvas
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] //2) # compute center X Y
white = (255, 255, 255) # create white color

# loop over increasing radii, from 25 pixels to 150 pixels in 25 pixel increments
for r in range(0, 175, 25):
    # draw a white circle with current radius size
    cv2.circle(canvas, (centerX, centerY), r, white) # center to draw circle around, r = radius

# show the circle
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# re-initialize canvas
canvas = np.zeros((300, 300, 3), dtype="uint8")

# draw 25 random circles
for i in range (0, 25): # 25 random circles
    # randomly generate radius between 5 and 200
    # generate random color, then pick a random point to draw
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3,)).tolist() # generate a number 0 to 255 and we need 3 numbers for BGR
    pt = np.random.randint(0, high=300, size=(2,)) # center XY coordinate, we want 2 values

    # draw random circles on canvas
    cv2.circle(canvas, tuple(pt), radius, color, -1) # pt is the center point, and -1 to fill in

# display it
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)