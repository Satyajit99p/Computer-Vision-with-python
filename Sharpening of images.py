import cv2
import numpy as np

image=cv2.imread('C:/Users/SATYAJIT/Pictures/download.png')

kernel=np.array([[-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1],
                 [-1,-1,25,-1,-1],
                 [-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1]])

image1=cv2.filter2D(image,-1,kernel)
cv2.imshow('filter',image1)
cv2.imshow('original',image)
cv2.waitKey()
cv2.destroyAllWindows()