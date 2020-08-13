import cv2
import numpy

color = cv2.imread('rgb1.png', 4)

cv2.namedWindow('Hari', 2)
cv2.imshow('Hari',color)

cv2.waitKey(0)
cv2.destroyAllWindows()

#gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
#cv2.imwrite('hari_gray.jpg', gray)

# b = color[:,:,0]
# g = color[:,:,1]
# r = color[:,:,2]

#rgba = cv2.merge((b,g,r,g))
#cv2.imwrite('rgba.png',rgba)
