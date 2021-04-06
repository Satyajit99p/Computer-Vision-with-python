import cv2
import numpy as np

image=cv2.imread('C:/Users/SATYAJIT/Pictures/download.png')
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

image1 =cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,5)

cv2.imshow('original',image)
cv2.imshow('mean',image1)

cv2.waitKey()
cv2.destroyAllWindows()