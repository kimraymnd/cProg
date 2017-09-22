from sys import stdin, stdout, argv


def main():

    # input via readline method
    file_input = open(argv[-1])
    n = file_input.readline()
    # n = stdin.readline()

    # array input similar method
    arr = [int(x) for x in file_input.readline().split()]


    # print answer via write
    # write method writes only
    # string operations
    # so we need to convert any
    # data into string for input
    stdout.write()

# call the main method
if __name__ == "__main__":
    main()
