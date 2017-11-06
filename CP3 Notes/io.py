# import inbuild standard input and output
from sys import stdin, stdout

def main():
    # input ends with (an array of) 0
    input_ = [int(x) for x in stdin.readline().split()]
    # test_cases = int(stdin.readline())

    while(any(input_)):

        # do stuff here
        # code
        input_ = [int(x) for x in stdin.readline().split()]

if __name__=="__main__":
    main()
