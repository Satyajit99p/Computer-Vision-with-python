import cv2
import numpy as np

def mouse_event(event,x,y,flag,params):
     if(event == cv2.EVENT_LBUTTONDOWN):
        str1=str(x)+","+str(y)
        cv2.putText(image,str1,(x,y),(cv2.FONT_HERSHEY_SIMPLEX),1,(45,34,23),2)     # to put text at the coordinate of mouse click
        points.append((x,y))
        if len(points)==2:
           cv2.rectangle(image,points[0],points[1],(0,255,0),3)   # to draw rectangle at two diagonal clicks 
           
           #to crop the selected rectange part out of image
           crop_image= image[points[-2][1]:points[-1][1],points[-2][0]:points[-1][0]]
           cv2.imshow('Frame',crop_image)
     cv2.imshow('Frame',image) 
    
     if (event == cv2.EVENT_MOUSEMOVE):                             # to drag and scribble on the image                                                     
        points.append((x,y))
        if len(points)>=2:
            cv2.line(image,points[-2],points[-1],(56,255,100),5)
     cv2.imshow('Frame',image)
    
     if (event == cv2.EVENT_RBUTTONDOWN):
        blue = image[y,x,0]
        green = image[y,x,1]
        red = image[y,x,2]
        str1 = str(blue)+","+str(green)+","+str(red)
        cv2.putText(image,str1,(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(160,100,155),3)     # to show the color matrix point for rigth clicked coordinate
        
        # to create a new frame of solid color of the coordinate when rmouse is clicked
        image1 = np.zeros((512,512,3),np.uint8)
        image1[:]=[blue,green,red]
        cv2.imshow('frame1',image1)
        
     cv2.imshow('Frame',image)

image=cv2.imread('Capture1.PNG')
points=[]

cv2.imshow('Frame',image)
cv2.setMouseCallback('Frame',mouse_event)

cv2.waitKey()
cv2.destroyAllWindows()