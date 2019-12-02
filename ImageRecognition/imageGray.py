import cv2
import numpy as np


img = cv2.imread('Hari.jpeg')
len(img)

# Height represents the number of pixel rows in the image or the number of pixels in each column of the image array.
# Width represents the number of pixel columns in the image or the number of pixels in each row of the image array.
# No of Channels represents the number of components used to represent each pixel. Red, Green and Blue channels.

print("Height, Width, No of Channels: ", img.shape)
print(img.dtype)    # Type of image
print(img.size)     #Total Pixels in the images

cv2.imshow("HariKrishna", img)
cv2.waitKey(0)


black = np.zeros([150,200,1],'uint8')
cv2.imshow("Black", black)

#print(black[0,0,:])
cv2.waitKey(0)
cv2.destroyAllWindows()
