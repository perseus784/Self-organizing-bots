import cv2
import numpy as np
import imutils
import matplotlib.pyplot as plt
from shapedetector import ShapeDetector
#find contours SBS hyp in a same function just mask as binary after that.
lower = {'red': (169, 100, 100), 'green': (65, 100, 100)}
upper = {'red': (189, 255, 255), 'green': (85, 255, 255)}
img=cv2.imread("triangles.png")
img = imutils.resize(img, width=640, height=480)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(img, lower["green"], upper["green"])
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
print cnts
sd=ShapeDetector()
if len(cnts) > 0:
    print "here"
    c = max(cnts, key=cv2.contourArea)
    shape=sd.detect(c)
    #print shape
    rect = cv2.minAreaRect(np.array(c))
    print rect
    rect=((int(rect[0][0]),int(rect[0][1])),(int(rect[1][0]),int(rect[1][1])))
    print rect
    ((x, y), radius) = cv2.minEnclosingCircle(c)
    M = cv2.moments(c)
    center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
    if radius > 10:
        cv2.circle(img, (int(x), int(y)), int(radius), (255, 0, 0), 2)
        cv2.rectangle(img,rect[0], rect[1], (0, 255, 0), 2)
        cv2.circle(img, center, 5, (0, 0, 0), -1)
cv2.imshow("img",img)
cv2.waitKey(0)