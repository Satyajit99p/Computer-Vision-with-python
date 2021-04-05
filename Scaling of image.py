import cv2
import numpy as np

image = cv2.imread('C:/Users/SATYAJIT/Pictures/download.png')

image1=cv2.resize(image,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)
cv2.imshow('linear',image1)
image1=cv2.resize(image,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_AREA)
cv2.imshow('area',image1)
image1=cv2.resize(image,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_NEAREST)
cv2.imshow('nearest',image1)
image1=cv2.resize(image,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_CUBIC)
cv2.imshow('cubic',image1)
image1=cv2.resize(image,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LANCZOS4)
cv2.imshow('lanc',image1)
    


#pyramid method
image1=cv2.pyrUp(image)   #pyrup to scale up the image an pyrdown o scale down the image

cv2.imshow('pyramid',image1)
cv2.imshow('original',image)
cv2.waitKey()
cv2.destroyAllWindows()
