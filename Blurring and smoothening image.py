import cv2
import numpy as np

image = cv2.imread('C:/Users/SATYAJIT/Pictures/download.png')

kernel_5x5 = (np.ones((5,5),np.uint8))/25
kernel_9x9 = (np.ones((9,9),np.uint8))/81

#method one, creating own kernels
image1=cv2.filter2D(image,-1,kernel_5x5)
image2=cv2.filter2D(image,-1,kernel_9x9)

#method 2.using function no need to cteate kernels
image3=cv2.blur(image,(5,5))
image4=cv2.GaussianBlur(image,(5,5),0)
image5=cv2.medianBlur(image,5)
image6=cv2.bilateralFilter(image,9,75,75)


cv2.imshow('original',image)
cv2.imshow('kernel_5x5',image1)
cv2.imshow('kernel_9x9',image2)
cv2.imshow('blur',image3)
cv2.imshow('gaussian blur',image4)
cv2.imshow('median blur',image5)
cv2.imshow('bilateral',image6)





cv2.waiKey()
cv2.destroyAllWindows()