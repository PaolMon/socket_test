import cv2 
from AES import AESCipher

en = AESCipher('unachiave')

vid_cap = cv2.VideoCapture(0) 

hasFrames,image = vid_cap.read()

c = en.encrypt(image)



