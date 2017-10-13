from sys import stdin, stdout
from collections import defaultdict

def main():
    #  numpad = {'ABC':2, 'DEF':3, 'GHI':4, 'JKL':5, 'MNO':6, 'PQRS':7, 'TUV':8, 'WXYZ':9}
    numpad = {'P':7, 'Q':7, 'R':7, 'S':7, 'T':8, 'U':8, 'V':8, 'W':9, 'X':9, 'Y':9, 'Z':9}
    for i in range(65,65+15):
        numpad[chr(i)] = int((i+1)/3)-20
    directory = defaultdict(list)
    extensionSet = set()
    for line in stdin:
        line = line.split()

        if(len(line) == 3):
            extensionSet.add(line[2])
            firstlast = str(numpad[line[0][0]])
            for ch in line[1]:
                # print(ch)
                firstlast += str(numpad[ch.upper()])
            directory[firstlast].append(line[2])
        else:
            output = []
            flag = False
            inp = line[0]
            if inp in extensionSet:
                print(inp)
            else:
                for val in list(directory):
                    if val.find(inp) == 0:
                        for x in directory[val]:
                            output.append(x)
                if len(output) == 0:
                    print(0)
                else:
                    print(" ".join(output))
            
if __name__=="__main__":
    main()
