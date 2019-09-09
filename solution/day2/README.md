### 基础：pull图片并打开

分组之后一名队员向GitHub上传图片，另一名队员pull图片，并用opencv打开

```
import numpy as np
import cv2

img = cv2.imread('image.jpg')
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

```

### 进阶：截取图片

```
import numpy as np
import cv2
img = cv2.imread("image.jpg")

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow("image", img)

cropImg = img[100:200, 0:50]
cv2.namedWindow('imagecrop', cv2.WINDOW_NORMAL)
cv2.imshow("imagecrop", cropImg)

cv2.imwrite("crop.jpg", cropImg) 

cv2.waitKey(0)
cv2.destroyAllWindows()

```

### 挑战：分割九宫格

```
import numpy as np
import cv2

img=cv2.imread("c:/Users/M/Desktop/img/c.jpg")

lenth=len(img)
width=len(img[0])

print("lenth",lenth)
print("width",width)

L=int(lenth/3)
W=int(width/3)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

for ln in range(3):
    for wn in range(3):
        cropImg=img[ln*L:(ln+1)*L,wn*W:(wn+1)*W]
        cv2.imshow("image",cropImg)
        cv2.waitKey(100)        
        filename="crop"+str(ln)+str(wn)+".jpg"
        print(filename)
        cv2.imwrite(filename,cropImg) 

cv2.destroyAllWindows()
```
