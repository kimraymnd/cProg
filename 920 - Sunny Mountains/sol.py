from sys import stdin, stdout
import math

def length_of_sunshine(startP, endP, h):
    dx, dy = abs(startP[0]-endP[0]), abs(startP[1]-endP[1])
    assert endP[1] > h
    return math.sqrt(dx*dx + dy*dy) * ((endP[1] - h)/float(dy))

def main():

    # input via input file
    # n = file_input.readline()
    # input via std in
    test_case = int(stdin.readline())

    while test_case > 0:
        # n is number of points
        n = int(stdin.readline())
        points = []
        # read in input
        for i in range(n):
            point = (stdin.readline())
            points.append([int(x) for x in point.split()])
            points = sorted(points, reverse=True)
        total_length = 0
        current_height = 0
        for i in range(int(n/2)):
            # assume that mountains are "jagged"
            if current_height < points[2*i+1][1]:
                x = length_of_sunshine(points[2*i], points[2*i+1], current_height)
                total_length += x
                current_height = points[2*i+1][1]

        stdout.write("%.2f\n" % total_length)
        test_case -= 1

    # print answer via write
    # write method writes only
    # string operations
    # so we need to convert any
    # data into string for input
    # stdout.write("\n")

# call the main method
if __name__ == "__main__":
    main()
