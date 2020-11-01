import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth) #Length id is 3
cap.set(4,frameHeight)  #Width id is 4
cap.set(10,150) #Brightness id is 10

myColors = [[24, 51, 0,  37, 97, 255],
[4, 146, 0, 14, 193, 255]]

def findColor(img, myColors):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower= np.array(myColors[0][0:3])
    upper= np.array(myColors[0][3:])
    mask = cv2.inRange(hsv, lower, upper)
    cv2.imshow("Image", mask)

while True:
    success, img = cap.read()
    findColor(img, myColors)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break




