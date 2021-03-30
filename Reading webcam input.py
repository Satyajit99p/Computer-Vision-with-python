import cv2

image=cv2.VideoCapture(0)   #creating object image of VideoCapture class
count=0

# to facilitate iterative image capturing until we press 'q'
while(True):
    count+=1
    
    #reading or starting our webcam
    check,frame=image.read()    #check - to check if the image is recorded
                                #frame -  matrix within which the image is stored
                                
    cv2.imshow('image',frame)
    if cv2.waitKey(1) == ord('q'): # continuously click images till q is pressed with framegap of 0.001 second
        break

    print(frame.shape)
    
    cv2.imwrite('my image'+str(count)+'.jpg',frame)

#shutting down the webcam
image.release()
cv2.destroyAllWindows()

