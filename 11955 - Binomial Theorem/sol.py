# import inbuild standard input and output
from sys import stdin, stdout

comb = [[0 for j in range(i+1)] for i in range(51)]

def many_C(n,k):
    # if we need many but not all C(n,k)
    global comb
    if n==0:
        comb[0][0] == 1
        return 1
    elif n>0 and k == 0:
        comb[n][0] = 1
        return 1
    elif n>0 and k == n:
        comb[n][n] = 1
        return 1
    else:
        if comb[n-1][k-1] == 0:
            comb[n-1][k-1] = many_C(n-1, k-1)
        if comb[n-1][k] == 0:
            comb[n-1][k] = many_C(n-1,k)
        comb[n][k] = comb[n-1][k-1] + comb[n-1][k]
        return(comb[n][k])

def exptostring(p):
    if p == 1: return ""
    return "^"+str(p)

def main():
    global comb

    # input_ = [int(x) for x in stdin.readline().split()]
    test_cases = int(stdin.readline())

    for case in range(test_cases):
        input_ = stdin.readline().strip()
        n_ind = input_.find("^")
        n = int(input_[n_ind+1:])

        expression = input_[1:n_ind-1].split("+")

        stdout.write("%s%d: " % ("Case ", case+1))

        if n==1:
            stdout.write("%s\n" % (input_[1:-3]))
        else:
            # ouput = str(expression[0]) + "^" + str(n)
            stdout.write("%s" % (str(expression[0]) + "^" + str(n) + "+"))
            # stdout.write("%s" % "")
            for k in range(n-1,0,-1):
                c = many_C(n,k)
                stdout.write("%s" % (str(c)+"*"+str(expression[0]) + exptostring(k) + "*" + expression[1] + exptostring(n-k)+"+"))

            stdout.write("%s\n" % (str(expression[1]) + "^" + str(n)))


if __name__=="__main__":
    main()
