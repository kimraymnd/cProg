'''
WIL: start i increasing from 0 and j decreasing from i to the beginning
    - j has to start close to i in order to fill the smaller gaps/subproblems first


'''

from sys import stdin, stdout

def main():

    n = int(stdin.readline().strip())
    H = [int(x) for x in stdin.readline().split()]
    arr = [[0 for x in range(2)] for x in range(n)]

    # for i in range(n):
    #     for j in range(i-1, -1, -1):

    for j in range(n,-1,-1):
        for i in range(j,n):
        # for j in range(i+1, n):
    # for j in range(n-1):
    #     for i in range(j+1,n):
            print (i, j)
            if H[i]>H[j]: arr[i][0] = max(arr[i][0], arr[j][1] + 1)
            elif H[i]<H[j]: arr[j][1] = max(arr[j][1], arr[i][0] + 1)

    output = ""
    for i in range(n):
        h = max(arr[i][0], arr[i][1])
        output = output + str(h) + " "

    print(arr)
    stdout.write(output.strip())

if __name__=="__main__":
    main()
