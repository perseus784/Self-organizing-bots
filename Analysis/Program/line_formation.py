import matplotlib.pyplot as plot
from matplotlib import collections  as mc
p=[2,6,45,34,89,71,3,77,51,60,79]
q=[12,78,34,01,56,83,56,9,66,74,22]
line=[]
distance=[]
new=[]
bots=11
x=100
y=100
#basic parameters
median=y/2
upper_range=x-(0.1*x)
lower_range=x-(0.9*x)
spacing=(upper_range-lower_range)/bots
z=lower_range
def line_skeleton(z=z):
    #for making line skeleton in any given x and y
    for i in range(bots):
        line.append([z,median])
        z=z+spacing
    return line
def dist_from_skeletonpoints():
    for i in range(bots):
        distance.append([p[i]-line[i][0],q[i]-line[i][1]])
    print distance
def line_scatter_plot(line=line):
    plot.scatter(p, q, s=60, marker='o')
    for j in line:
        plot.scatter(j[0],j[1],s=200,marker='x',c='r')
    plot.show()
def magnitude_pathplotting():
    for k in range(bots):
        # distance magnitude
        new.append([[line[k][0], line[k][1]], [p[k], q[k]]])
    print new
    lc = mc.LineCollection(new, colors='g', linewidths=2)
    fig, ax = plot.subplots()
    print fig
    ax.add_collection(lc)
    ax.autoscale()
    ax.margins(0.1)
def assign_points():
    plot.scatter(p, q, s=60, marker='o')
    for i in range(bots):
        p[i] = line[i][0]
        q[i] = line[i][1]
    plot.scatter(p, q, s=70, marker='*', c='r')
    plot.show()
if __name__=="__main__":
    line_skeleton(z)
    dist_from_skeletonpoints()
    line_scatter_plot()
    magnitude_pathplotting()
    assign_points()