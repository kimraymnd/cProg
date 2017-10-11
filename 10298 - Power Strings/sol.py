from sys import stdin, stdout
def main():
    global count
    s = stdin.readline().strip()
    while(s[0] != '.'):
        n = len(s)
        i = (s+s).find(s, 1, -1)
        stdout.write("%d\n" % (1)) if (i==-1) else stdout.write("%d\n" % (int(len(s) / i)))
        s = stdin.readline().strip()
if __name__=="__main__":
    main()
