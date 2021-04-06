import cv2
import numpy as np

kernel=np.ones((5,5),np.uint8)

image=cv2.imread('C:/Users/SATYAJIT/Pictures/download.png')

image1=cv2.erode(image,kernel,iterations=1)
image2=cv2.dilate(image,kernel,iterations=1)

image3=cv2.morphologyEx(image,cv2.MORPH_OPEN,kernel)
image4=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)

cv2.imshow('erosion',image1)
cv2.imshow('ilation',image2)
cv2.imshow('original',image)
cv2.imshow('open',image3)
cv2.imshow('close',image4)

cv2.waitKey()
cv2.destroyAllWindows()
