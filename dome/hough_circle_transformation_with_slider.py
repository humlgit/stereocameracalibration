import numpy as np
import cv2 as cv

def empty(a):
    pass

img = cv.imread("dome/sphere3.jpg", cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img = cv.medianBlur(img,5)
cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)

cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars",640,240)
cv.createTrackbar("centerDist","TrackBars",10,1000,empty)
cv.createTrackbar("param1","TrackBars",200,500,empty)
cv.createTrackbar("param2","TrackBars",30,50,empty)
cv.createTrackbar("minRadius","TrackBars",10,100,empty)
cv.createTrackbar("maxRadius","TrackBars",0,600,empty)

while True:
    cimg = cv.cvtColor(img,cv.COLOR_GRAY2BGR)
    centerDist = cv.getTrackbarPos("centerDist","TrackBars")
    param1 = cv.getTrackbarPos("param1", "TrackBars")
    param2 = cv.getTrackbarPos("param2", "TrackBars")
    minRadius = cv.getTrackbarPos("minRadius", "TrackBars")
    maxRadius = cv.getTrackbarPos("maxRadius", "TrackBars")
    #cv.setTrackbarMin("maxRadius", "TrackBars", minRadius)
    print(centerDist,param1,param2,minRadius,maxRadius)

    circles = cv.HoughCircles(img,cv.HOUGH_GRADIENT,1,centerDist,param1=param1,param2=param2,minRadius=minRadius,maxRadius=maxRadius)
    circles = np.uint16(np.around(circles))
    if circles.any():
        for i in circles[0,:]:
            # draw the outer circle
            cv.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    cv.imshow('detected circles',cimg)
    cv.waitKey(1)
