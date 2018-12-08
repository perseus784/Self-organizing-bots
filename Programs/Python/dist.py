import numpy as np
import skeleton_algorithms as s
import matplotlib.pyplot  as plt
from matplotlib import collections  as mc
bot_points=[[72,43],[22,87],[92,13],[33,55],[71,02],[13,55],[77,1],[32,33],[91,64],[2,4],[99,100]]
t=bot_points
line=[]
skelton=s.line_skeleton()
#skelton=s.rectangular_wave(li=s.line_skeleton())
def nearest_neighbours(skeleton,temp):
    #find euclidian distance  eu_dist=sqrt((x1-y1)*2-(x2-y2)*2)
    dist_dict=[]
    #mutable list should be assigned properly
    temp=temp[:]
    print temp
    global t
    for i in skeleton:
         distance=[]
         for j in temp:
               dis=np.linalg.norm(np.array(i)-np.array(j))
               distance.append([dis,j])

         new1=[k[1] for k in sorted(distance)][0]
         print new1
         dist_dict.append(new1)
         temp.remove(new1)
    return dist_dict
n=nearest_neighbours(skelton,bot_points)
[plt.scatter(m[0],m[1]) for m in bot_points]
[plt.scatter(l[0],l[1],c='r') for l in skelton]
for k in range(11):
    line.append([skelton[k],n[k]])
lc = mc.LineCollection(line, colors='g', linewidths=2)
print lc
fig, ax = plt.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)
[plt.scatter(m[0],m[1],s=100) for m in bot_points]
[plt.scatter(l[0],l[1],c='r',marker='*',s=200) for l in skelton]
plt.show()
