# CP3 Chapter 5 code in python
import random
import math

# 5.3 Java BigInteger Class
# p202 Exercise 5.3.2.4 Miller Rabin's Algorithm
def isProbablyPrime(n, k):
    """
    input 1: n > 3, odd integer
    input 2: determines accuracy of test, P(isprime) = 1 - (1/2)^k
    output: 0 if n is composite, otherwise 1
    runtime: O(k lg^3 n)
    """
    print("n is", n, ", k is", k)
    d = n-1
    r = 0
    while(d%2 == 0):
        r += 1
        d = int(d/2)

    for i in range(k):
        cont_flag = False
        a = random.randrange(2,n-1)
        x = a**d % n
        if x == 1 or x == n-1:
            continue
        for j in range(r-1):
            x = x*x % n
            if x == 1:
                return False
            if x == n-1:
                cont_flag = True
                break
        if cont_flag:
            cont_flag = False
            continue
        return False
    return True

# 5.4 Combinatorics
# 5.4.1 Fibonacci
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    x, y = 0, 1
    for i in range(n-1):
        z = x+y
        x = y
        y = z
    return y

def binet(n):
    phi = (1+math.sqrt(5))/2
    return (phi**n - (-phi)**(-n)) / math.sqrt(5)

def zeckendorf(n):
    """Every positive integer can be written in a way as a sum of one or more distinct Fibonacci numbers such that the sum does not include any two consecutive Fibonacci numbers."""
    fiblist = []
    summand = []
    i = 0
    while(fib(i) < n):
        fiblist.append(fib(i))
        i += 1
    m = n
    for k in range(i-1,0,-1):
        if fiblist[k] <= m:
            summand.append(fiblist[k])
            m -= fiblist[k]
    return summand

# 5.4.2 Binomial Coefficients
from functools import reduce

def C(n,k):
    # if we need to compute single C(n,r)
    n = min(n, k-n)
    if r == 0: return 1
    numer = reduce((lambda x,y: x*y), range(n, n-r, -1))
    denom = reduce((lambda x,y: x*y), range(1, r+1))
    return numer//denom

# memoize in comb[] where n is max n used
# comb = [[0 for j in range(i+1)] for i in range(n)]
def many_C(n,k):
    # if we need many but not all C(n,k)
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

# if we need to compute all C(n,k), O(n^2)
def pascals_triangle(n):
    PT = [[0 for j in range(i+1)] for i in range(n)]
    for i in range(n):
        if i == 0:
            PT[0][0] = 1
            continue
        PT[i][0] = 1
        PT[i][i] = 1
        for j in range(1,i):
            PT[i][j] = PT[i-1][j-1] + PT[i-1][j]
    return(PT)

# 5.4.3 Catalan Numbers
def catalan(n):
    if n == 0: return 1
    return C(2*n, n) // (n+1)

# memoize in comb[] where n is max n used
# cat = [0 for i in range(n)]
def several_cat(n):
    # if we need to compute several values of catalan(n)
    for i in range(n+1):
        if i==0:
            cat[0] = 1
        else:
            cat[i] = int(2*(2*i-1)/(i+1) * cat[i-1])
    return cat[n]

# 5.5.1 Prime Numbers
from bitarray import bitarray

ub = 1000000 # list of primes in [0,1000000]
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

def isPrime(n):
    global ub
    if n <= ub: return bs[n]
    for i in range(len(primes)):
        if n % primes[i] == 0: return False
    return True

# sieve(ub)
# isPrime(2147483647)

# 5.5.2 GCD and LCM, O(log n)
def gcd(a,b):
    return a if (b == 0) else gcd(b, a%b)
def lcm(a,b):
    return a * (b // gcd(a,b))

# 5.5.3 Factorial
def range_prod(lo,hi):
    if lo+1 < hi:
        mid = (hi+lo)//2
        return range_prod(lo,mid) * range_prod(mid+1,hi)
    if lo == hi:
        return lo
    return lo*hi

def treefactorial(n):
    if n < 2:
        return 1
    return range_prod(1,n)

# 5.5.4
def primeFactors(n):
    factor_list = []
    factor_dict = dict()
    pf_i = 0
    pf = primes[pf_i]
    while(pf * pf <= n):
        if n % pf == 0: factor_dict[pf] = 0
        while n % pf == 0:
            n //= pf
            factor_list.append(pf)
            factor_dict[pf] += 1
        pf_i += 1
        pf = primes[pf_i]
    if n != 1:
        factor_list.append(n)
        factor_dict[n] = 1
    return factor_list, factor_dict

# 5.5.6 Functions Involving Prime Factors
def numPF(n):
    '''count the number of prime factors of n'''
    pf_i = 0
    pf = primes[pf_i]
    ans = 0
    while(pf * pf <= n):
        while (n % pf == 0):
            n //= pf
            ans += 1
        pf_i += 1
        pf = primes[pf_i]
    if n != 1:
        ans += 1
    return ans

def numDiffPF(n):
    '''count the number of distinct prime factors of n'''
    pf_i = 0
    pf = primes[pf_i]
    ans = 0
    while(pf * pf <= n):
        if (n%pf == 0): ans += 1
        while (n % pf == 0):
            n //= pf
        pf_i += 1
        pf = primes[pf_i]
    if n != 1:
        ans += 1
    return ans

def sumPF(n):
    '''sum the prime factors of n'''
    pf_i = 0
    pf = primes[pf_i]
    ans = 0
    while(pf * pf <= n):
        while (n % pf == 0):
            n //= pf
            ans += pf
        pf_i += 1
        pf = primes[pf_i]
    if n != 1:
        ans += n
    return ans

def numDiv(n):
    '''count the number of divisors of n'''
    pf_i = 0
    pf = primes[pf_i]
    ans = 1
    while(pf * pf <= n):
        power = 0
        while (n % pf == 0):
            n //= pf
            power += 1
        ans *= (power+1)
        pf_i += 1
        pf = primes[pf_i]
    if n != 1:
        ans *= 2
    return ans

def sumDiv(n):
    '''sum the number of divisors of n'''
    pf_i = 0
    pf = primes[pf_i]
    ans = 1
    while(pf * pf <= n):
        power = 0
        while (n % pf == 0):
            n //= pf
            power += 1
        ans *= (pf**(power+1)-1)//(pf-1)
        pf_i += 1
        pf = primes[pf_i]
    if n != 1:
        ans *= (n**2 - 1)//(n-1)
    return ans

def eulerPhi(n):
    '''count the number of relatively prime integers < n'''
    pf_i = 0
    pf = primes[pf_i]
    ans = n
    while(pf * pf <= n):
        if n % pf == 0: ans -= ans//pf
        while (n % pf == 0):
            n //= pf
        pf_i += 1
        pf = primes[pf_i]
    if n != 1:
        ans -= ans//n
    return ans

# 5.5.8 Modulo Arithmetic
# may need to compute intermediate results mod n

# 5.5.9 Linear Diophantine Equation
# ex. solving ax + by = c
x, y, d = 0,0,0
def extendedEuclid(a, b):
    global x, y, d
    if b == 0:
        x,y,d = 1,0,a
        return
    extendedEuclid(b, a%b)
    x1 = y
    y1 = x - (a // b) * y
    x = x1
    y = y1

# 5.7 Cycle-Finding
# given f(x) and x_0, find
#     mu = start of cycle
#     lambda = cycle length
# 5.7.1 Using Efficient Data-Structure (use dict or set)

# 5.7.2 Floyd's Cycle-Finding Algorithm
def floydCycleFinding(x0):
    # f defined prior
    # find k * mu, where cycle is
    t = f(x0)
    h = f(f(x0))
    while (t != h):
        t = f(t)
        h = f(f(h))
    # finding mu, h and t move at same speed
    mu = 0
    h = f(x0)
    while (t != h):
        t = f(t)
        h = f(h)
        mu += 1
    # finding l, h moves, t stays
    l = 1
    h = f(t)
    while (t != h):
        h = f(h)
        l += 1
    return mu, l
