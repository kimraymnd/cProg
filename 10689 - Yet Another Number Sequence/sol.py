# import inbuild standard input and output
from sys import stdin, stdout
import math

def main():
    # input ends with (an array of) 0
    case = int(stdin.readline())
    # pisano period: the last 1/2/3/4 digits repeat w/ period 60/300/1500/15000
    pp = [60, 300, 1500, 15000]
    for c in range(case):
        input_ = [int(x) for x in stdin.readline().split()]
        a = input_[0]
        b = input_[1]
        n = input_[2]
        m = input_[3]

        n = n % pp[m-1]
        if n == 0:
            stdout.write("%d\n" % (a % (10**m)))
            continue
        for i in range(n-1):
            sum_ = a+b
            a = b
            b = sum_ % (10**m)

        stdout.write("%d\n" % (b))

if __name__=="__main__":
    main()
