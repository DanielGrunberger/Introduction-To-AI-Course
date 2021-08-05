import random
import matplotlib.pyplot as plt

width = 100
height = 100
gap = 50
size = 50

def distance(x, y):
    return sum( (x[i]-y[i])**2 for i in range(len(x)))

def create_dataset():
    ds = []
    for i in range(size):
        ds += [[random.randrange(0,width) , random.randrange(0,(height-gap)//2)]]
        ds += [[random.randrange(0,width) , random.randrange(((height+gap)//2),height)]]
    return ds

def point2int(p):
    return p[1] * width + p[0]

def nearest(point, centers):
    m = 0
    for i in range(1, len(centers)):
        if distance(point, centers[i]) < distance(point, centers[m]):
            m = i
    return m

def find_centers(clusters):
    centers = []
    for cluster in clusters:
        center = [0] * len(cluster[0])
        for point in cluster:
            for i in range(len(point)):
                center[i] += point[i]/len(cluster)
        centers += [center]
    return centers

def kmeans(ds, centers):
    while True:
        clusters =[]
        for i in range(len(centers)):
            clusters += [[]]
        for i in range(len(ds)):
            clusters[nearest(ds[i], centers)] += [ds[i]]
        new_centers = find_centers(clusters)
        if new_centers == centers:
            return [centers, clusters]
        centers = new_centers

def experiment(plot = False):
    ds = create_dataset()
    centers = []
    for i in range(len(ds)-1):
        for j in range(i+1, len(ds)):
            if ds[j] != ds[i]:
                x = [ds[i][:],ds[j][:]]
                c = kmeans(ds, x)
                sorted_c = sorted(c[0], key = point2int)
                if sorted_c not in centers:
                    if plot:
                        show(c)
                    centers += [sorted_c]
    return len(centers)

def show(c):
    for p in c[1][0]:
        plt.plot(p[0], p[1], "bs")
    for p in c[1][1]:
        plt.plot(p[0], p[1], "rs")
    plt.plot(c[0][0][0], c[0][0][1], "b^")
    plt.plot(c[0][1][0], c[0][1][1], "r^")
    plt.show()

c = 0
for i in range(1):
    c += experiment(plot=True)
print(c)



