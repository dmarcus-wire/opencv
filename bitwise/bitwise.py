# USAGE
# python bitwise.py

# best understood visually
# ON = 255, white color
# OFF = 0, black color
# import necessary packages
import numpy as np # allocating memory to draw shapes
import cv2 # for binding

# draw a rectangle
rectangle = np.zeros((300, 300), dtype="uint8") # 300x300 canvas
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1) # draw rectangle starting at x=25,7=25 to x=275,y=275, white=255 color, -1 to draw rectangle in
cv2.imshow("Rectangle", rectangle)

# draw a circle
circle = np.zeros((300, 300), dtype="uint8") # 300x300 canvas, x=150,y=150
cv2.circle(circle, (150, 150), 150, 255, -1) # x=150,y=150, radius 150, white color 255, -1 filled in
cv2.imshow("Circle", circle)

# a bitwise 'AND' is only 'True' when both input are 'ON'
# cv2.bitwise examines every pixel in the rectangle and circle
# if BOTH pixels have a value > 0 than the pixel is ON (i.e. 255)
bitwiseAnd = cv2.bitwise_and(rectangle, circle) # showing only where all pixels are ON
cv2.imshow("AND", bitwiseAnd)
cv2.waitKey(0)

bitwiseOr = cv2.bitwise_or(rectangle, circle)
cv2.imshow("OR", bitwiseOr)
cv2.waitKey(0)

bitwiseXor = cv2.bitwise_xor(rectangle, circle)
cv2.imshow("XOR", bitwiseXor) # exclusive or two values cannot be ON
cv2.waitKey(0)

bitwiseNot = cv2.bitwise_not(circle)
cv2.imshow("NOT", bitwiseNot)
cv2.waitKey(0)


