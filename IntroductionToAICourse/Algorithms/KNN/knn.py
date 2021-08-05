import heap
import math
import random

def make_points(points, n, d, k):
#craetes a file (points) with n points in a d-dimensional space, in k clusters
    f=open(points, "w")
    for i in range(n):
        s=""
        x=random.randrange(0,k) #random.randrange creates a random number 0..k-1
        for j in range(d):
        # creates numbers around x*100
            s=s+str(100*x+random.randrange(-10,10))+" "
        f.write(s+str(x)+"\n")
    f.close()
    
def distance(x,y,method="E"):
    if method=="E":#Euclidean distance
        dis=0
        for i in range(len(x)):
            dis+=(x[i]-y[i])**2
        return math.sqrt(dis)
    if method=="M":#Manhattan distance
        dis=0
        for i in range(len(x)):
            dis+=abs(x[i]-y[i])
        return dis

def majority(h):
    a=[]
    while not heap.is_empty(h):
        a+=[heap.remove(h)[1]]
    a.sort()
    count=0
    maj=a[0]
    max=1
    for i in range(1,len(a)):
        if a[i]==a[i-1]:
            count+=1
            if count>max:
                max=count
                maj=a[i]
        else:
            count=1
    return maj

def knn(k, points, x):
    h=heap.create()
    f=open(points, "r")
    s=f.readline()
    while s!="":
        s=s.split()
        for i in range(len(s)):
            s[i]=int(s[i])
        d=distance(s[:-1],x)
        heap.insert(h,[d,s[-1]])
        if heap.size(h)>k:
            heap.remove(h)
        s=f.readline()
    f.close()
    return majority(h)


make_points("points.txt", 200000, 4, 3)
print(knn(3,"points.txt",[50,50,50,50]))
    


            
        
        
