from sys import stdin, stdout
from bitarray import bitarray

ub = 10000000 # list of primes in [0,1000000]
bs = bitarray(10000010)
primes = []

def sieve(upperbound):
    global bs
    size = upperbound + 1
    bs.setall(True)
    bs[0] = False
    bs[1] = False
    for i in range(2,size+1,1):
        if bs[i]:
            for j in range(i*i,size+1,i):
                bs[j]=0
            primes.append(int(i))

def getExcess(n):
    pf_i = 0
    pf = primes[pf_i]
    ans = 0
    while(pf * pf <= n):
        if (n % pf == 0): ans -= 1
        while (n % pf == 0):
            n //= pf
            ans += 1
        pf_i += 1
        pf = primes[pf_i]
    if n != 1:
        ans += 1
    return ans


def main():
    sieve(ub)
    range_ = [int(x) for x in stdin.readline().split()]
    while(any(range_)):
        max_i = -1
        max_e = 1
        counter = 0
        excess = map(getExcess, range(range_[0], range_[1]+1))
        for i in excess:
            if i > max_e:
                max_e = i
                max_i = counter
            counter += 1
        stdout.write("%d\n" % (range_[0]+max_i))

        range_ = [int(x) for x in stdin.readline().split()]

if __name__=="__main__":
    main()
