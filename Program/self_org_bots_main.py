import numpy as np
import matplotlib.pyplot as plt
import cv2
import threading as thr
import time as ti
import imutils
import urllib2 as url
bot_points=[[72,43],[22,87],[92,13],[12,55],[71,02],[13,55],[77,1],[32,33],[91,64],[2,4],[99,100]]
t=bot_points
#initialisations
line=[]
pos=[]
posi=[]
cent=[]
clr_id={}
distance=[]
dist=[]
new=[]
bots=5
u=1
v=1
d=1
e=1
s_lim=5
x=640
y=480
cap=cv2.VideoCapture(1)
lower = {'red': (166, 100, 100), 'green': (40, 100, 100), 'blue': (100, 100,100), 'yellow': (8,100, 100), 'orange': (-6,100,100)}
upper = {'red': (186, 255, 255), 'green': (65, 255, 255), 'blue': (120, 255, 255), 'yellow': (28, 255, 255), 'orange': (14,255,255)}
center_bot=int((bots-1)/2)
median=int(y/2)
upper_range=x-(0.1*x)
lower_range=x-(0.9*x)
spacing=(upper_range-lower_range)/bots
z=int(lower_range)
def bot70(x,y):#robot protocols
    return 0
def bot71(x,y):#robot protocols
    return 0
def bot72(x,y):#robot protocols
    return 0
def bot73(x,y):#robot protocols
    return 0
def bot74(x,y):#robot protocols
    return 0
#test(can be ignored if not necessary)
def overall():
    url.urlopen("http://192.168.43.70/LED=ON")
    t.sleep(0.9)
    url.urlopen("http://192.168.43.70/LED=OFF")
    url.urlopen("http://192.168.43.72/LED2=ON")
    t.sleep(0.4)
    url.urlopen("http://192.168.43.72/LED=OFF")
    url.urlopen("http://192.168.43.73/LED=ON")
    t.sleep(0.8)
    url.urlopen("http://192.168.43.73/LED=OFF")
    url.urlopen("http://192.168.43.73/LED1=ON")
    t.sleep(0.7)
    url.urlopen("http://192.168.43.73/LED=OFF")
    url.urlopen("http://192.168.43.71/LED1=ON")
    t.sleep(0.8)
    url.urlopen("http://192.168.43.71/LED=OFF")
    url.urlopen("http://192.168.43.72/LED=ON")
    t.sleep(0.8)
    url.urlopen("http://192.168.43.72/LED=OFF")
    url.urlopen("http://192.168.43.70/LED1=ON")
    t.sleep(0.8)
    url.urlopen("http://192.168.43.70/LED=OFF")
    url.urlopen("http://192.168.43.72/LED1=ON")
    t.sleep(0.3)
    url.urlopen("http://192.168.43.72/LED=OFF")
    url.urlopen("http://192.168.43.71/LED=ON")
    t.sleep(0.7)
    url.urlopen("http://192.168.43.71/LED=OFF")
    url.urlopen("http://192.168.43.73/LED2=ON")
    t.sleep(0.6)
    url.urlopen("http://192.168.43.73/LED=OFF")
    url.urlopen("http://192.168.43.71/LED2=ON")
    t.sleep(0.7)
    url.urlopen("http://192.168.43.71/LED=OFF")
    url.urlopen("http://192.168.43.70/LED2=ON")
    t.sleep(0.8)
    url.urlopen("http://192.168.43.70/LED=OFF")
#get image from cam    
def get_image():
    #_,img=cap.read()
    img=cv2.imread("img1.jpg")
    _=True
    if _:
        return img
    else:
        print "camera cannot be accessed"
        return None
#skeletal structures    
def line_skeleton(z=z):
    #for making line skeleton in any given x and y
    for i in range(bots):
        line.append([z,median])
        z=int(z+spacing)
    return line
def rectangular_wave(space=s_lim,li=line):
    global u,v,d,e
    '''               ##########
                    #
         ##########              '''
    l_skeleton = li
    for i in l_skeleton[:center_bot]:
        i[1]=int(i[1]-space)
    for j in l_skeleton[center_bot+1:]:
        j[1]=int(j[1]+space)
    wave_skeleton = l_skeleton
    #[plot.scatter(k[0], k[1],s=70,c='r') for k in wave_skeleton]
    for l in wave_skeleton[:center_bot]:
        l[0]=int(l[0]+spacing)
    for n in wave_skeleton[center_bot+1:]:
        n[0]=int(n[0]-spacing)
    #[plot.scatter(o[0], o[1],c='c',s=100,marker='x') for o in wave_skeleton]
    y_high=median+space
    y_low=median-space
    temp=(center_bot-1)/2
    print wave_skeleton[center_bot]
    x_high=wave_skeleton[center_bot][0]+temp*spacing
    print wave_skeleton[center_bot]
    x_low=wave_skeleton[center_bot][0]-temp*spacing
    up_limbot=center_bot+1
    low_limbot=center_bot+2
    remain_bots=(bots-2)/2
    stem=remain_bots/2
    stem_spacing_y=(y_high-y_low)/stem
    stem_spacing_x = (x_high - median) / stem
    for r in wave_skeleton[:stem]:
        r[0]=int(x_low)
        r[1]=int(r[1]+u*stem_spacing_y)
        u=u+1
    for s in wave_skeleton[-(stem):]:
        s[0]=int(x_high)
        s[1] =int(s[1]-v*stem_spacing_y)
        v=v+1
    [plt.scatter(o[0], o[1], c='c', s=100, marker='x') for o in wave_skeleton]
    return wave_skeleton
#application of NN algorithm to reduce time and save power. K=1.
def nearest_neighbours(skeleton,temp):
    posi=[]
    #find euclidian distance  eu_dist=sqrt((x1-y1)*2-(x2-y2)*2)
    #mutable list should be assigned properly
    temp=temp[:]
    t=temp
    for i in xrange(len(t)):
        distance=[]
        for j in temp:
            dis = np.linalg.norm(np.array(skeleton[i]) - np.array(j))
            distance.append([dis,j])
        pos=[k[1] for k in sorted(distance)][0]
        posi.append(pos)
        temp.remove(pos)
    return posi
def color_centers(x,lower,upper):
    mask = cv2.inRange(x, lower, upper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        rect=cv2.minAreaRect(np.array(c))
        print rect
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 10:
            cv2.circle(g, (int(x), int(y)), int(radius),(0, 255, 255), 2)
            cv2.circle(g, center, 5, (0, 255, 0), -1)
            return center
    else:return 0
if __name__=="__main__":
    g = get_image()
    g = imutils.resize(g, width=640, height=480)
    hsv = cv2.cvtColor(g, cv2.COLOR_BGR2HSV)
    for clr, ran in lower.iteritems():
        clr_centr = color_centers(hsv, lower[clr], upper[clr])
        if clr_centr == 0:
            pass
        else:
            cent.append(list(clr_centr))
            clr_id[clr] = tuple(clr_centr)
    lin = line_skeleton()
    arranged = nearest_neighbours(lin, cent)
    [cv2.circle(g, tuple(ke), 6, (0, 0, 255), 2) for ke in lin]
    for ind, ar in enumerate(arranged):
        cv2.circle(g, tuple(ar), 7, (0, 255, 225), -1)
        # cv2.line(g,tuple(lin[ind]), tuple(ar), 7)


    def set_clr(skel, arranged, clr_id, dist):
        for s, a, d in zip(skel, arranged, dist):
            for key in clr_id.keys():
                print key
                if clr_id[key] == tuple(a):
                    print "here"
                    clr_id[key] = [s, a, d[0], d[3]]
        return clr_id

    #calculate angle for each bot to target point
    def finding_angles(line, points):
        for i, j in zip(line, points):
            hyp = (np.linalg.norm(np.array(i) - np.array(j)))
            opp = (np.linalg.norm(np.array((j[0], median)) - np.array(j)))
            adj = (np.linalg.norm(np.array(i) - np.array((j[0], median))))
            angle = 180 - (90 + np.degrees((np.arccos((adj / hyp)))))
            dist.append([hyp, opp, adj, angle])
        return dist


    print finding_angles(lin, arranged)
    final_dict = set_clr(lin, arranged, clr_id, dist)
    #format:[color:orgin,destination,distance,angle]
    print final_dict
    for k, va in final_dict.iteritems():
        cv2.line(g, tuple(va[0]), tuple(va[1]), (255, 0, 0), 4)

    for key,value in final_dict.iteritems():
        if key=='blue':
            x1=thr.Thread(target=bot70,args=(value[2],value[3]))
        if key=='green':
            x2=thr.Thread(target=bot71,args=(value[2],value[3]))
        if key=='red':
            x3=thr.Thread(target=bot72,args=(value[2],value[3]))
        if key=='yellow':
            x4=thr.Thread(target=bot73,args=(value[2],value[3]))
        if key=='orange':
            x5=thr.Thread(target=bot74,args=(value[2],value[3]))
    cv2.imshow("go", g)
    cv2.waitKey(0)
    x1.start()
    x2.start()
    x3.start()
    x4.start()
    x5.start()



