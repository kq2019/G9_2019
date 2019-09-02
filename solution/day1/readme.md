### 基础：打开图片

```python
import numpy as np
import cv2

img = cv2.imread('你的图片路径', 0)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 进阶：拷贝图片内容

```python
import numpy as np
import cv2

img = cv2.imread('你的图片路径', 0)
img[0:50, 0:50] = img[100:150, 100:150]
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 挑战：人脸识别

```python
import cv2

img = cv2.imread('你的图片路径')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
face_cascade = cv2.CascadeClassifier('你的数据集路径')

faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(5, 5),
)

print("发现{0}个人脸！".format(len(faces)))
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+w), (0,255,0), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
