
import cv2

import numpy as np


vid_cap = cv2.VideoCapture(0) 


hasFrames,image = vid_cap.read()
print(image.shape)
print(image.dtype)
k = image.tobytes()
ka = bytearray(k)
print(len(ka))

y = np.frombuffer(k, dtype=np.uint8, count=-1)
y=np.reshape(y, (480, 640, 3))

cv2.imshow('image',y)

cv2.waitKey(0)