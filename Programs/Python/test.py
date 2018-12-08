import numpy as np
import cv2
from matplotlib import pyplot as plt
import imutils
import heirarchial_clustering as hc
img = cv2.imread("blue.jpg")
w=500
h=500
img=imutils.resize(img,width=w,height=h)
img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower = {'red': (168, 100, 100), 'green': (24, 100, 100),'blue':(104, 100, 100),'yellow':(9, 100, 100),'pink':(153, 100, 100),'mil_green':(58, 100, 100)}
upper = {'red': (188, 255, 255), 'green': (44, 255, 255),'blue':(124, 255, 255),'yellow':(29, 255, 255),'pink':(173, 100, 100),'mil_green':(78, 100, 100)}
mask = cv2.inRange(img, lower['yellow'], upper['yellow'])
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)

def euclidean_dist(x,y):
    dist=np.linalg.norm(x-y)
    return dist

def find_ref_point(basept,hyp_pts):
    min_dict={np.linalg.norm(basept-hyp_pts[0]):hyp_pts[0],np.linalg.norm(basept-hyp_pts[1]):hyp_pts[1]}
    return min_dict

def color_centers():
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        rect=cv2.minAreaRect(np.array(c))
        print rect
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 10:
            cv2.circle(img, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.circle(img, center, 5, (0, 255, 0), -1)
            return center
    else:return 0

dst = cv2.cornerHarris(mask,2,3,0.04)
#result is dilated for marking the corners, not important
dst = cv2.dilate(dst,None)
x,y = np.nonzero(dst > 0.1* dst.max())
coordinates = zip(x, y)
new=[]
for i in coordinates:
    new.append(list(i))
actual_points=hc.auto_cluster(radius=5,data=np.array(new))# coverting range of points to a single point using heirarchial cluster.
print actual_points
hyp_dict={}

for key,val in actual_points.iteritems():
    for key1,val1 in actual_points.iteritems():
        hyp_dict[euclidean_dist(val,val1)]=[val,val1]


#print dist_dict
hyp=max(hyp_dict)
print "here",hyp
hyp_values=hyp_dict[hyp]
print hyp_values
cent=actual_points
#IMPORTANT TRANSFORMATION REQUIRED
[plt.scatter(y,-x,10) for x,y in new]

point=(w/2,h/2)
cv2.circle(img,point, 5, (0, 255, 0), -1)
point=np.array(list(point))
print point
hyp_dist=find_ref_point(point,hyp_values)
ref_point=hyp_dist[min(hyp_dist)]
print ref_point
f_point=hyp_dist[max(hyp_dist)]
print f_point
s_point=[f_point[0],ref_point[1]]
cv2.circle(img,(int(s_point[1]),int(s_point[0])), 5, (0, 255, 0), -1)
print s_point
adj=np.linalg.norm(ref_point-s_point)
print adj
hypo=np.linalg.norm(ref_point-f_point)
print hypo
angle = 180 - (90 + np.degrees((np.arccos((adj / hypo)))))
print angle
center=color_centers()
print center
#inverse logic
inv_logic=[]
for k,v in actual_points.iteritems():
    inv_logic.append(v)
print "hyper"
print hyp_values
inv_logic=np.array(inv_logic)
index = np.argwhere(inv_logic==hyp_values[0])
#y = np.delete(inv_logic, index)

for hv in hyp_values:
    index = np.argwhere(inv_logic == hv)
    yu = np.delete(inv_logic, index)
    print yu
print inv_logic

#motor logic
#forawrd speed: ~5cm/s
#angular speed: ~48*/s
if point[1]>center[1]:
    if point[0]>center[0]:
        motor=("left",angle)
    else:motor=("right",angle)
else:
    if point[0]>center[0]:
        motor=("right",angle)
    else:motor=("left",angle)
print motor

for c in cent:
    plt.scatter(cent[c][1],-cent[c][0] , s=200, marker='*')
# Threshold for an optimal value, it may vary depending on the image.

img[dst>0.1*dst.max()]=[250,0,0]
cv2.imshow('dst',img)
plt.show()

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()