from math import sqrt
from numpy import array

#D - P -V((D-P).vnorm)

def dot(a,b):
    return(sum([i*j for i,j in zip(a,b)]))

def mag(a):
    return(sqrt(dot(a,a)))

def mindist(P,V,D):
    minDVect = D-P-V*(dot(D-P,V)/mag(V))
    mindist = mag(minDVect)
    return(mindist)

if __name__ == '__main__':
    P = array([2,4,8])
    V = array([-3,4,1])
    D = array([1,0,0])

    print(mindist(P,V,D))
