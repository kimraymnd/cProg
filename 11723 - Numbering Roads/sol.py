# import inbuild standard input and output
from sys import stdin, stdout
import math

def main():
    # input ends with (an array of) 0
    input_ = [int(x) for x in stdin.readline().split()]
    case = 1
    while(any(input_)):
        # do stuff here
        # code
        R = input_[0]
        N = input_[1]

        if R > (N)*27:
            stdout.write("%s%d%s\n" % ("Case ", case, ": impossible"))
        else:
            num_suffix = math.ceil((R-N)/N)
            stdout.write("%s%d%s%d\n" % ("Case ", case, ": ", num_suffix))

        case += 1
        input_ = [int(x) for x in stdin.readline().split()]

if __name__=="__main__":
    main()
