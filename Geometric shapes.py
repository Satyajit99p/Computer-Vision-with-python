import numpy as np
import cv2

#creating a black background image
img1 = np.zeros((512,512,3),np.uint8)

img=cv2.imread('Capture1.png')
print(img.shape)

#creating a line
cv2.line(img,(10,10),(255,255),(56,255,122),5)  #(object,start_pixel coordinate, end_pixel coordinate,line color,thickness in px)
cv2.line(img1,(10,10),(255,255),(56,255,122),5)

#creating arrowhead line
cv2.arrowedLine(img,(10,10),(255,255),(56,255,122),5)
cv2.arrowedLine(img1,(10,10),(255,255),(56,255,122),5)

#creating a rectangle
cv2.rectangle(img,(100,20),(200,40),(0,255,0),3)      #(object ,upperleft diagonal point,lower diagonal right )
cv2.rectangle(img1,(100,20),(200,40),(0,255,0),3)

#creating a circle
cv2.circle(img,(150,150),50,(0,255,0),5)       # (object, circle center, radius)
cv2.circle(img1,(150,150),50,(0,255,0),5)

# to make a solid shape just change thickness parameter to -1
cv2.circle(img,(100,150),50,(0,255,0),-1)       # (object, circle center, radius)
cv2.circle(img1,(150,100),50,(0,255,0),-1)

#to put text
cv2.putText(img,'shapes',(150,150),cv2.FONT_ITALIC,3,(0,255,6),5 )

cv2.imshow('capture_shape',img)
cv2.imshow('shape',img1)
cv2.waitKey()
cv2.destroyAllWindows()