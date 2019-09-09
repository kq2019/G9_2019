import numpy as numpy
import cv2


img = cv2.imread('Master.jpg')
cv2.rectangle(img,(695,475),(745,425),(0,255,0),3)
cv2.rectangle(img,(695,525),(745,475),(0,255,0),3)
cv2.rectangle(img,(695,425),(745,375),(0,255,0),3)
cv2.imshow('Master.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
