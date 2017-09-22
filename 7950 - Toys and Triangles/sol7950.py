from sys import stdin, stdout, argv
from math import sqrt
from operator import itemgetter
from itertools import permutations

class Point:
    "2D point with non-integer coordinates"
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x)+", "+str(self.y)+")"
    def __eq__(self,p):
        return (abs(self.x - p.x) < EPS and abs(self.y - p.y) < EPS)

# class

def circ_circ_intersection(c1, r1, c2, r2):
    x1,y1,r1 = c1[0], c1[1], r1
    x2,y2,r2 = c2[0], c2[1], r2
    dx,dy = x2-x1,y2-y1
    d = sqrt(dx*dx+dy*dy)
    if d > r1+r2:
        print "#1"
        return None # no solutions, the circles are separate
    if d < abs(r1-r2):
        print "#2"
        return None # no solutions because one circle is contained within the other
    if d == 0 and r1 == r2:
        print "#3"
        return None # circles are coincident and there are an infinite number of solutions

    a = (r1*r1-r2*r2+d*d)/(2*d)
    h = sqrt(r1*r1-a*a)
    xm = x1 + a*dx/d
    ym = y1 + a*dy/d
    xs1 = xm + h*dy/d
    xs2 = xm - h*dy/d
    ys1 = ym - h*dx/d
    ys2 = ym + h*dx/d
    return (xs1,ys1),(xs2,ys2)
#     return (float(xs1),float(ys1)),(float(xs2),float(ys2))

def triIneq(a,b,c):
    return (a+b>c and a+c>b and b+c>a)

def testTI(r):
    '''tests triangle inequality on sliding window(2) of triangle lengths'''
    assert len(r)%2 == 1
    for i in range((len(r)-1)/2):
        if not triIneq(r[2*i],r[2*i+1],r[2*i+2]):
            return False #[r[2*i],r[2*i+1],r[2*i+2]]
    return True

def getVertex(p, r):
    '''return max x value of third vertex'''
    assert isinstance(p,list) and isinstance(r,list) and len(p)==2 and len(r)==2
    return max(circ_circ_intersection(p[0],r[0],p[1],r[1]), key=itemgetter(0))

def getMaxX(r):
    assert testTI(r)
    p = [(0,0)]
    p.append((0,r[0]))
    for i in range((len(r)-1)/2):
#         sol = max(circ_circ_intersection(p[i],r[2*i+1],p[i+1],r[2*i+2]), key=itemgetter(0))
#         sol = max(circ_circ_intersection(p[0],r[2*i+1],p[1],r[2*i+2]), key=itemgetter(0))
#         print(p, r[2*i+1:2*i+3])
#         print "getVertex output:",getVertex(p, r[2*i+1:2*i+3])
        p.append(getVertex(p, r[2*i+1:2*i+3]))
        p = p[1:]
#         print "new centers:",p
    return p[-1][0]

def main():
    # opens last file as input txt argument
    file_input = open(argv[-1])
    # puts each line of file_input into array n
    n = file_input.readlines()
    # for each line in n
    for case in n:
        # turn case into an array of int-casted elements 
        case = [int(i) for i in case.split()]
        lengths = case[1:]
        perm_len = case[0] if case[0]%2==1 else case[0]-1
        max_x = 0
        for i in permutations(lengths,perm_len):
            if testTI(list(i)):
#         assert testTI(list(i))
                temp = getMaxX(list(i))
                max_x = temp if temp > max_x else max_x
        stdout.write("%.2f\n" % max_x)

# call the main method
if __name__ == "__main__":
    main()
