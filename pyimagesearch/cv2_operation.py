# import the necessary packages
import imutils
import cv2
# load the input image and show its dimensions, keeping in mind that
# images are represented as a multi-dimensional NumPy array with
# shape no. rows (height) x no. columns (width) x no. channels (depth)
image = cv2.imread("iron_chic.jpg")
(h, w, d) = image.shape
print("width={}, height={}, depth={}".format(w, h, d))
# display the image to our screen -- we will need to click the window
# open by OpenCV and press a key on our keyboard to continue execution

cv2.imshow("Image", image)

#Slice the image
roi = image[60:160, 320:420]
# cv2.imshow("ROI", roi)

# Resize the Image
resized = cv2.resize(image, (200, 200))
# cv2.imshow("Fixed Resizing", resized)

r = 300.0 / w
dim = (300, int(h * r))
resized = cv2.resize(image, dim)
# cv2.imshow("Aspect Ratio Resize", resized)

resized1 = imutils.resize(image, width=300, height=900)
# cv2.imshow("Imutils Resize", resized1)

# rotation can also be easily accomplished via imutils with less code
rotated = imutils.rotate(image, -45)
# cv2.imshow("Imutils Rotation", rotated)


# OpenCV doesn't "care" if our rotated image is clipped after rotation
# so we can instead use another imutils convenience function to help
# us out
rotated = imutils.rotate_bound(image, 45)
# cv2.imshow("Imutils Bound Rotation", rotated)

# apply a Gaussian blur with a 11x11 kernel to the image to smooth it,
# useful when reducing high frequency noise
blurred = cv2.GaussianBlur(image, (11, 11), 0)
# cv2.imshow("Blurred", blurred)

output = image.copy()
cv2.rectangle(output, (320, 60), (420, 160), (0, 0, 255), 2)
# cv2.imshow("Rectangle", output)

# draw a blue 20px (filled in) circle on the image centered at
# x=300,y=150
output = image.copy()
cv2.circle(output, (300, 150), 20, (255, 0, 0), -1)
# cv2.imshow("Circle", output)


# draw green text on the image
output = image.copy()
cv2.putText(output, "OpenCV + Party Celebration!!!", (10, 25),
	cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
cv2.imshow("Text", output)

cv2.waitKey(0)
