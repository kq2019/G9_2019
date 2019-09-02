import cv2 

face = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
 
 
sample_image = cv2.imread('mind2.jpg')
print (sample_image)
faces = face.detectMultiScale(sample_image,scaleFactor=1.1,minNeighbors=5,minSize=(10,10))
 
print (faces)

for(x,y,w,h) in faces:
    cv2.rectangle(sample_image, (x,y), (x+y,y+h), (0,255,0), 2)
 
cv2.imwrite('peopleResult.png',sample_image)