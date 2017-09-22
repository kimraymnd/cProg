from sys import stdin, stdout

def main():
    # testcases = int(stdin.readline())
    # for tc in range(testcases):
    #     datanum = int(stdin.readline())
    #     data = []
    #     for dc in range(datanum):
    #         data.append(list(map(int, stdin.readline().split())))
    #     # print(type(data))
    #     print(data,"\n")
    # stdout.write();
    n = 100
    count = 0
    for i in range(n,-1,-1):
        stdout.write("%d %d\n" % (count, i))
        stdout.write("%d %d\n" % (count+i,0))
        if i == n:
            count += 1
        if i == 1:
            break
        count += n


if __name__ == "__main__":
    main()
