import cv2
import numpy as np

image=cv2.imread('C:/Users/SATYAJIT/Pictures/download.png')
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

ret,image1=cv2.threshold(image,140,255,cv2.THRESH_BINARY) # convert pixels below 140 to 0 an above 140 to 1 
# essentially gives a image higlighting only dark and light parts
ret,image2=cv2.threshold(image,140,255,cv2.THRESH_BINARY_INV)
ret,image3=cv2.threshold(image,140,255,cv2.THRESH_TOZERO)
ret,image4=cv2.threshold(image,140,255,cv2.THRESH_TRUNC)
ret,image5=cv2.threshold(image,140,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('original',image)
cv2.imshow('binary',image1)
cv2.imshow('binary_inv',image2)
cv2.imshow('tozero',image3)
cv2.imshow('trunc',image4)
cv2.imshow('tozero_inv',image5)

cv2.waitKey()
cv2.destroyAllWindows()