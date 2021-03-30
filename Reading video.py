import cv2

image=cv2.VideoCapture(0)   #creating object image of VideoCapture class
fourcc_code=cv2.VideoWriter_fourcc(*"XVID")
video=cv2.VideoWriter('my video.avi',fourcc_code,30,(640,480)) #( name,format,framerate,size)

count=0

# to facilitate iterative image capturing until we press 'q'
while(True):
    count+=1
    
    #reading or starting our webcam
    check,frame=image.read()    #check - to check if the image is recorded
                                #frame -  matrix within which the image is stored
     
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)  #toconvert video into grayscale
    video.write(frame)          #to compile all the frames into a video                           
    cv2.imshow('image',frame)
    if cv2.waitKey(1) == ord('q'): # continuously click images till q is pressed with framegap of 0.001 second
        break

    print(frame.shape)
    
    cv2.imwrite('my image'+str(count)+'.jpg',frame)

#shutting down the webcam
video.release()
image.release()
cv2.destroyAllWindows()

