import cv2
import numpy as np

image = cv2.imread('C:/Users/SATYAJIT/Pictures/download.png')

row,col,ch=image.shape
x=20
y=30
# the signs of x and y decide which quadrant of a graph (or corner) the image will be shifted to)
T=np.float64([[1,0,x],[0,1,y]])

while(True):              #to animate the image framewise(shifting according to x and y)
    #to crop or shift an image
    image1=cv2.warpAffine(image,T,(col,row))
    
    cv2.imshow('frame',image)
    cv2.imshow('frame1',image1)
    
    k=cv2.waitKey()
    if k==ord('q'):
        break
    x=x+1
    y=y+1
cv2.destroyAllWindows()
