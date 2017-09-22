from sys import stdin, stdout
import math

def distance(a,b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def main():

    # input via readline method
    n = stdin.readlines()
    # n = stdin.readline()
    input = []
    for line in n:
        input.append(tuple([int(x) for x in line.split()]))
    dist = [0]*10

    for i in range(len(n)-1):
        mindist = -1
        for j in range(len(n)-1):
            p_dist = distance(input[i],input[j])
            if (p_dist < mindist or mindist < 0) and i != j:
                mindist = p_dist
        if mindist < 10:
            dist[int(math.floor(mindist))] += 1
    for i in range(10):
        stdout.write("%4s"% dist[i])

# call the main method
if __name__ == "__main__":
    main()
