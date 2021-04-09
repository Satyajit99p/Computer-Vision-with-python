import cv2
import numpy as np

image=cv2.imread('C:/Users/SATYAJIT/Pictures/download.png')
 
#the pyrup and pyrdown methods are used to scale up and scale down the image

image1=cv2.pyrDown(image)
image2=cv2.pyrUp(image)


cv2.imshow('original',image)
cv2.imshow(str(image1.shape),image1)
cv2.imshow(str(image2.shape),image2)
cv2.waitKey()
cv2.destroyAllWindows()