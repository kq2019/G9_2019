import numpy as np 
import cv2 
img = cv2.imread('mind.jpg')

cv2.rectangle(img,(100,0),(0,50),(0,255,0),3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()