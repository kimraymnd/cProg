from sys import stdin, stdout
import math

def intersect_val(a):
    cIn = a[0]
    for i in range(1,len(a)):
        # find intersection of current intersection and a[i]
        # disjoint, total interval will be 0
        if (cIn[1] < a[i][0]) or (cIn[0] > a[i][1]):
            return 0
        cIn = [max(cIn[0], a[i][0]), min(cIn[1], a[i][1])]
    return abs(cIn[0]-cIn[1])

def main():
    tc = int(stdin.readline())
    while(tc != 0):
        x, y, z = [], [], []
        for cubes in range(tc):
            data = [int(x) for x in stdin.readline().split()]
            # make x, y, z intervals from data
            x.append([data[0],data[0]+data[3]])
            y.append([data[1],data[1]+data[3]])
            z.append([data[2],data[2]+data[3]])
        # find volume of intersection, write to stdout
        stdout.write("%d\n" % (intersect_val(x) * intersect_val(y) * intersect_val(z)))

        tc = int(stdin.readline())

if __name__ == "__main__":
    main()
