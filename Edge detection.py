import cv2
import numpy as np

image=cv2.imread('C:/Users/SATYAJIT/Pictures/download.png')

image1=cv2.Canny(image,30,100)  # to decide the borders and edges

cv2.imshow('original',image)
cv2.imshow('canny',image1)
cv2.waitKey()
cv2.destroyAllWindows()