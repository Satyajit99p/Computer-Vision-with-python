import cv2
import numpy as np

image1 = cv2.imread('C:/Users/SATYAJIT/Pictures/download.png')
image2 = cv2.imread('C:/Users/SATYAJIT/Pictures/pie chart.png')
image3 = cv2.imread('C:/Users/SATYAJIT/Pictures/Capture1.PNG') 

#image2=image2+100      # increase all the shade of each pixel by 100
#image4=image3*2        # create a new image of existing image by multiply pixel shade by 2

image5 = np.ones(image3.shape,np.uint8)   #ceating an empy image
image5=image5*100
image3=cv2.add(image3,image5)              #increasing the density of each pixel by factor of image 5
# adding two images need to have same shape

#overlappting two images(ading one image as watermark over another)
image1=cv2.resize(image1,(512,512))
image3=cv2.resize(image3,(512,512))
image6 = cv2.addWeighted(image3,0.7,image1,0.3,0)
#both images must be of same size

cv2.imshow('frame1',image1)
cv2.imshow('frame2',image2)
cv2.imshow('frame3',image3)
#cv2.imshow('frame4',image4)
cv2.imshow('frame5',image5)
cv2.imshow('frame6',image6)

cv2.waitKey()
cv2.destroyAllWindows()