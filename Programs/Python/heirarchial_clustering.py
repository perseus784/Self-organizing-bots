import numpy as np
import matplotlib.pyplot as plt
import random as r

#this lets the program decide number of groups involved in the given dataset
#setting all the points as centroids
centroids = {}

def auto_cluster(radius,data):
    global centroids

    for i in range(len(data)):
        centroids[i] = data[i]

    while True:
        new_centroids=[]
        #checking all the points whether it is in radius and assign to to that centroid
        for j in centroids:
            in_radius=[]
            centroid=centroids[j]
            for point in data:
                if np.linalg.norm(point-centroid)<radius:
                    in_radius.append(point)
            #finding mean
            new_centroid=np.average(in_radius,axis=0)
            new_centroids.append(tuple(new_centroid))
        #collect all the final centroids for each grp
        uniques=sorted(list(set(new_centroids)))
        prev_centroids=dict(centroids)
        centroids={}
        #fil with new centroids
        for i in range(len(uniques)):
            centroids[i]=np.array(uniques[i])
        opt=True
        #chech whether the centroid is optimized
        for i in centroids:
            if not np.array_equal(centroids[i],prev_centroids[i]):
                opt=False
            if not opt:
                break
        if opt:break
    return centroids

if __name__=="__main__":
    data = [[61, 148], [61, 149], [61, 150], [62, 147], [62, 148], [62, 149], [62, 150], [63, 147], [63, 148],
            [63, 149], [63, 150], [64, 147], [64, 148], [64, 149], [64, 150], [65, 147], [65, 148], [65, 149],
            [65, 150], [149, 436], [149, 437], [149, 438], [150, 366], [150, 367], [150, 368], [150, 436], [150, 437],
            [150, 438], [150, 439], [151, 366], [151, 367], [151, 368], [151, 436], [151, 437], [151, 438], [151, 439],
            [152, 366], [152, 367], [152, 368], [152, 436], [152, 437], [152, 438], [152, 439], [175, 147], [175, 148],
            [175, 149], [175, 150], [175, 264], [175, 265], [175, 266], [175, 267], [176, 147], [176, 148], [176, 149],
            [176, 150], [176, 264], [176, 265], [176, 266], [176, 267], [177, 147], [177, 148], [177, 149], [177, 150],
            [177, 264], [177, 265], [177, 266], [177, 267], [178, 147], [178, 148], [178, 149], [178, 264], [178, 265],
            [178, 266], [230, 366], [230, 367], [230, 368], [230, 369], [231, 366], [231, 367], [231, 368], [231, 369],
            [232, 366], [232, 367], [232, 368], [232, 369], [233, 366], [233, 367], [233, 368]]
    data = np.array(data)
    centroids = {}

    cent = auto_cluster(radius=5,data=data)
    print centroids
    print(len(cent))  # no. of centroids
    # plots
    [plt.scatter(x[0], x[1], s=50, c='g') for x in data]
    for c in cent:
        plt.scatter(cent[c][0], cent[c][1], s=200, marker='*')
    plt.show()