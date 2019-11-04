#!/usr/bin/python

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
scaling_factor = 0.5

while True:
   ret, frame = cap.read()
   #gray = cv2.cvtcolor(frame, cv2.COLOR_BGR2GRAY)

   frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor,interpolation=cv2.INTER_AREA)

   cv2.imshow('frame', frame)
   #cv2.imshow('gray', gray)
   
   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
