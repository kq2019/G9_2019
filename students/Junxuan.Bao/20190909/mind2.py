import numpy as np 
import cv2 
img = cv2.imread('mind.jpg')

cv2.rectangle(img,(50,0),(0,50),(0,255,0),3)
cv2.rectangle(img,(50,50),(0,100),(0,255,0),3)
cv2.rectangle(img,(50,100),(0,150),(0,255,0),3)

cv2.rectangle(img,(100,0),(50,50),(0,255,0),3)
cv2.rectangle(img,(100,50),(50,100),(0,255,0),3)
cv2.rectangle(img,(100,100),(50,150),(0,255,0),3)

cv2.rectangle(img,(150,0),(100,50),(0,255,0),3)
cv2.rectangle(img,(150,50),(100,100),(0,255,0),3)
cv2.rectangle(img,(150,100),(100,150),(0,255,0),3)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()