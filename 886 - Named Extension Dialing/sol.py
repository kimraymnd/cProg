from sys import stdin, stdout
from collections import defaultdict

def main():
    #  creating numpad dictionary
    numpad = {'P':7, 'Q':7, 'R':7, 'S':7, 'T':8, 'U':8, 'V':8, 'W':9, 'X':9, 'Y':9, 'Z':9}
    for i in range(65,65+15):
        numpad[chr(i)] = int((i+1)/3)-20

    directory = defaultdict(list)

    # set for extensions
    extensionSet = set()

    #reading in input
    for line in stdin:
        line = line.split()

        # input is directory line
        if(len(line) == 3):
            extensionSet.add(line[2])
            # add numerical first letter of first name
            firstlast = str(numpad[line[0][0]])
            # add numerical last name
            for ch in line[1]:
                firstlast += str(numpad[ch.upper()])
            # map numerical key to extension
            directory[firstlast].append(line[2])

        # input is user query
        else:
            output = []
            inp = line[0]
            # query is an extension
            if inp in extensionSet:
                stdout.write("%s\n"%(inp))
            else:
                # check if we can find query in each key of dir
                for val in list(directory):
                    if val.find(inp) == 0:
                        # if found, append to output
                        for i in directory[val]:
                            output.append(i)
                # we find nothing
                if len(output) == 0:
                    stdout.write("0\n")
                # we have something; join
                else:
                    stdout.write("%s\n" % (" ".join(output)))
    # print(directory)
    return 0
if __name__=="__main__":
    main()
