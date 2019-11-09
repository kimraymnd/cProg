from sys import stdin, stdout
import math

# def test_command(grid, command):


def main():
    dim = [int(x) for x in stdin.readline().split()]
    while(len(dim) != 0):
        grid = []
        for row in range(dim[0]):
            grid.append(stdin.readline().split())
        command = stdin.readline()[:-1] # take care of trailing newline
        for row in range(dim[0]):
            print(grid[row])
        print()

        dim = [int(x) for x in stdin.readline().split()]

if __name__ == "__main__":
    main()
