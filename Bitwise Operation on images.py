import cv2
import numpy as np

image1 = cv2.imread('C:/Users/SATYAJIT/Pictures/Capture1.PNG')

image2 = np.zeros(image1.shape,np.uint8)
image3 = np.zeros(image1.shape,np.uint8)

cv2.rectangle(image2,(50,50),(150,150),(255,255,255),-1) # make an rectangle
cv2.circle(image3,(125,125),50,(255,255,255),-1)         # make a circle

image4=cv2.bitwise_and(image3,image2)                     #output the area common to both the image
image5=cv2.bitwise_or(image3,image2) 
image6=cv2.bitwise_xor(image3,image2) 
image7=cv2.bitwise_not(image2) 

cv2.imshow('frame1',image2)
cv2.imshow('frame2',image3)
cv2.imshow('frame3',image4)
cv2.imshow('frame4',image5)
cv2.imshow('frame5',image6)
#cv2.imshow('frame6',image7)


cv2.waitKey()
cv2.destroyAllWindows()