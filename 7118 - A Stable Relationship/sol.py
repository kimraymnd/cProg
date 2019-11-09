from sys import stdin, stdout
from itertools import combinations

EPS = 1e-9

def main():
    dim = [int(x) for x in stdin.readline().split()]
    while(any(dim)):
        building = [[['.' for x in range(dim[0])] for y in range(dim[1])] for z in range(dim[2])]

        # building [height] [length] [width]
        topple = True
        count = 0
        C = [0,0]
        base_vert = []
        for z in range(dim[2]):
            for x in range(dim[1]):
                building[z][x] = stdin.readline().strip()
                for y in range(dim[0]):
                    if building[z][x][y] == '#':
                        if z == 0:
                            base_vert.append([x,y])
                        count += 1
                        C[0] += x
                        C[1] += y
        C = [x/float(count) for x in C]
        print(base_vert, C)
        print()
        # print(base_vert[0][1]== C[2])

        # The object will not topple if and only if there exists a triangle strictly containing C, with each of the three vertices lying under one of the printed blocks of the bottom layer. (The vertices may lie under any combination of 1, 2, or 3 such blocks.)

        #case 1 block
        for vert in base_vert:
            if C == vert:
                print("same!")
                # topple = False
                stdout.write("%s\n" % ("Will not topple"))
                return 0

        #case 2 blocks C lies on line
        n = len(base_vert)
        for pair in combinations(base_vert,2):
            crossprod = (C[1]-pair[0][1])*(pair[1][0]-pair[0][0]) - (C[0]-pair[0][0])*(pair[1][1]-pair[0][1])
            if abs(crossprod) < EPS:
                dotprod = (C[0] - pair[0][1]) * (pair[1][0] - pair[0][0]) + (C[1] - pair[0][1])*(pair[1][1] - pair[0][1])
                if dotprod > EPS:
                    lensq = (pair[1][0]-pair[0][0])*(pair[1][0]-pair[0][0]) + (pair[1][1]-pair[0][1])*(pair[1][1]-pair[0][1])
                    if dotprod - lensq < EPS:
                        stdout.write("%s\n" % ("Will not topple"))
                        return 0

        #case 3 blocks C lies in triangle
        


        dim = [int(x) for x in stdin.readline().split()]

if __name__=="__main__":
    main()
