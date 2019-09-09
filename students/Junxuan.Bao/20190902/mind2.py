import numpy as np 
import cv2 
img = cv2.imread('mind.jpg',0)
img[0:50,0:50]=img[100:150,100:150]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
