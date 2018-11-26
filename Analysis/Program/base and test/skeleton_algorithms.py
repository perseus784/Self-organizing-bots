#Algorithm that gives skeleton points for LINE type and S type formation
import matplotlib.pyplot as plot
#sample data points
line=[]
distance=[]
new=[]
bots=11
u=1
v=1
d=1
e=1
s_lim=5
x=100
y=100
center_bot=int((bots-1)/2)
median=int(y/2)
upper_range=x-(0.1*x)
lower_range=x-(0.9*x)
spacing=(upper_range-lower_range)/bots
z=int(lower_range)
def line_skeleton(z=z):
    #for making line skeleton in any given x and y

    for i in range(bots):
        line.append([z,median])
        z=int(z+spacing)
    return line
def rectangular_wave(space=s_lim,li=line):
    global u,v,d,e
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
    [plot.scatter(o[0], o[1], c='c', s=100, marker='x') for o in wave_skeleton]
    return wave_skeleton

if __name__=="__main__":
    Line_skeleton=line_skeleton()
    l=Line_skeleton
    [plot.scatter(q[0], q[1], c='r', s=100, marker='o') for q in l]
    plot.show()
    S_skeleton=rectangular_wave( )
    [plot.scatter(p[0], p[1], c='g', s=300, marker='x') for p in S_skeleton]
    plot.show()