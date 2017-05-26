import matplotlib.pyplot as plot
import random as r
from matplotlib import collections  as mc
import line_formation as lf
p=[2,6,45,34,89,71,3,77,51,60,79]
q=[12,78,34,01,56,83,56,9,66,74,22]
line=[]
distance=[]
new=[]
#min number of bots for s_formation will be 7 or >(2n-1)
bots=11
x=100
y=100
s_lim=5
median=y/2
center_bot=((bots-1)/2)
upper_range=x-(0.1*x)
lower_range=x-(0.9*x)
spacing=(upper_range-lower_range)/bots
line_skeleton=lf.line_skeleton(lower_range)
#end of skeleton formation
#[plot.scatter(m[0],m[1]) for m in line_skeleton]
def rectangular_wave(space=s_lim):
    '''               ##########
                    #
         ##########              '''
    for i in line_skeleton[:center_bot]:
        i[1]=(i[1]-space)
    for j in line_skeleton[center_bot+1:]:
        j[1]=(j[1]+space)
    wave_skeleton = line_skeleton
    [plot.scatter(k[0], k[1],s=70,c='r') for k in wave_skeleton]
    for l in wave_skeleton[:center_bot]:
        l[0]=(l[0]+spacing)
    for n in wave_skeleton[center_bot+1:]:
        n[0]=(n[0]-spacing)
    [plot.scatter(o[0], o[1],c='c',s=100,marker='x') for o in wave_skeleton]
    print wave_skeleton
    print center_bot,wave_skeleton[center_bot],median
    y_high=median+space
    y_low=median-space
    print y_high,y_low
    temp=(center_bot-1)/2
    x_high=wave_skeleton[center_bot][0]+temp*spacing
    x_low=wave_skeleton[center_bot][0]-temp*spacing
    print x_high,x_low
    wave_skeleton[0]=[x_low,median]
    wave_skeleton[1]=[x_low,y_high]
    wave_skeleton[-1]=[x_high,median]
    wave_skeleton[-2]=[x_high,y_low]
    [plot.scatter(p[0], p[1],c='g',s=200,marker='x') for p in wave_skeleton]
    s_skeleton=wave_skeleton
if __name__=="__main__":
    rectangular_wave()
    plot.show()