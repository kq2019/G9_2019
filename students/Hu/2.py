import numpy as np
import cv2

img = cv2.imread('1.jpg')
cv2.rectangle(img,(332,118),(444,230),(0,255,0),3)
cv2.rectangle(img,(332,232),(444,351),(0,255,0),3)
cv2.rectangle(img,(446,118),(562,232),(0,255,0),3)
cv2.rectangle(img,(446,232),(562,352),(0,255,0),3)
cv2.rectangle(img,(567,118),(681,232),(0,255,0),3)
cv2.rectangle(img,(562,351),(681,437),(0,255,0),3)
cv2.rectangle(img,(332,351),(444,437),(0,255,0),3)
cv2.rectangle(img,(444,351),(562,437),(0,255,0),3)
cv2.rectangle(img,(562,232),(681,352),(0,255,0),3)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destoryAllWindows()
