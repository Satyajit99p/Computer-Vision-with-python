import cv2
import numpy as np

image = cv2.imread('C:/Users/SATYAJIT/Pictures/download.png')

row,col,ch=image.shape

angle=0

while(True):
    
    if(angle == 360):
        angle =0
    
    R=cv2.getRotationMatrix2D((row/2,col/4),angle,0.75)
    
    image1 = cv2.warpAffine(image,R,(col,row))
    
    cv2.imshow('frame1',image)
    cv2.imshow('frame2',image1)
    k=cv2.waitKey(1)
 
    if (k==ord('q')):
        break
    angle=angle+1
cv2.destroyAllWindows()
