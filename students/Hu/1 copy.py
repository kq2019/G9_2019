import numpy as np
import cv2


img = cv2.imread('1.jpg')
font = cv2.FONT_HERSHEY_SIMPLEX
for i in range(3):
    for j in range(3):
        cv2.rectangle(img,(200*j,200*i),(200*(j+1), 200*(i+1)),(0,255,0),3)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
