import numpy as np
import cv2
import time as t
import urllib2 as url
from matplotlib import pyplot as plt
import imutils
import heirarchial_clustering as hc
img = cv2.imread("new1.JPG")
w=500
h=500
img=imutils.resize(img,width=w,height=h)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = {'org': (3, 100, 100),'dest':(80, 100, 100),'blue':(104,100,100)}
upper = {'org': (23, 255, 255),'dest':(100, 255, 255),'blue':(124,255,255)}
speed=68
angular_speed=46
def forward(distance):
    time=distance/speed
    url.urlopen("http://10.0.0.20/LED=ON")
    t.sleep(time)
    url.urlopen("http://10.0.0.20/LED=OFF")
    pass
def left(angle):
    time=angle/angular_speed
    url.urlopen("http://10.0.0.20/LED1=ON")
    t.sleep(time)
    url.urlopen("http://10.0.0.20/LED=OFF")
    pass
def right(angle):
    time = angle / angular_speed
    url.urlopen("http://10.0.0.20/LED2=ON")
    t.sleep(time)
    url.urlopen("http://10.0.0.20/LED=OFF")
    pass
def color_centers(x,lower,upper):
    mask = cv2.inRange(x, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(cnts) > 0:
        print "yes"
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 1:
            cv2.circle(img, (int(x), int(y)), int(radius),(0, 255, 255), 2)

            cv2.circle(img, center, 5, (0, 255, 0), -1)
            return center
    else:return 0
dest_center=np.array(color_centers(img,lower["dest"],upper["dest"]))
print dest_center
origin_center=np.array(color_centers(img,lower["org"],upper["org"]))
print origin_center
right_pt=[dest_center[0],origin_center[1]]
print right_pt
hyp=np.linalg.norm(origin_center-dest_center)
adj=np.linalg.norm(right_pt-origin_center)
angle = np.degrees((np.arccos((adj / hyp))))
print hyp,adj,angle
#1cm=10px
#motor functions
'''
left(angle)
forward(hyp)
right(angle)'''





'''
#corner detecttion
mask = cv2.inRange(img, lower['green'], upper['green'])
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)
dst = cv2.cornerHarris(mask,2,3,0.04)
dst = cv2.dilate(dst,None)
x,y = np.nonzero(dst > 0.1* dst.max())
coordinates = zip(x, y)
img[dst>0.1*dst.max()]=[250,0,0]
new=[]
for i in coordinates:
    new.append(list(i))
actual_points=hc.auto_cluster(radius=5,data=np.array(new))# coverting range of points to a single point using heirarchial cluster.
print actual_points'''

cv2.imshow("demo",img)
cv2.waitKey(0)