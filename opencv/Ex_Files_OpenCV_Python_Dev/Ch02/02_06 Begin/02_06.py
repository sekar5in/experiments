import numpy as np
import cv2

image = cv2.imread("hari.jpg")
cv2.imshow('hari', image)

blur = cv2.GaussianBlur(image,(5,55),0)
cv2.imshow('hari_b',  blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
