import cv2                  #importing necessary module

#read the image from local irectory
image=cv2.imread('C:/Users/SATYAJIT/Pictures/Saved Pictures/816872.jpg')

#display the image
cv2.imshow('cars',image)
cv2.waitKey()
cv2.destroyAllWindows()  #closes the winow on clickin any button

print(image.shape)

cv2.imwrite('cars1.jpg',image)

cv2.imread('./cars1.jpg')
cv2.imshow('cars',image)
cv2.waitKey(5000)       #decifies the time for which the image window is open in miliseconds
cv2.destroyAllWindows()

# convert the image into black and white
bw=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('cars',bw)
cv2.waitkey()
cv2.destroyAllWindows()
print(bw.shape)

#isolate and highlight each of the central colors i.e. Red Blue Green
image=cv2.imread('./cars1.jpg')
B,G,R=cv2.split(image)
print(B.shape)
cv2.imshow('original',image)
cv2.imshow('Red',R)
cv2.imshow('Blue',B)
cv2.imshow('Green',G)
cv2.waitKey()
cv2.destroyAllWindows()

#merge each color with adjustments to specific shades
merge=cv2.merge(R,G+100,B+100)
cv2.imshow('merged',merge)
cv2.waitKey()
cv2.destroyAllWindows()