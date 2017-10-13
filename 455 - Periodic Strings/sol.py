from sys import stdin, stdout

def main():
    num_test_case = int(stdin.readline())
    stdin.readline()
    for inp in stdin:
        s = inp.strip()
        if len(s)==0:
            stdout.write("\n")
            continue
        n = (s+s).find(s,1,-1)
        stdout.write("%d\n" % len(s)) if n==-1 else stdout.write("%d\n" % n)
    return 0
if __name__=="__main__":
    main()
