from sys import stdin, stdout
import math
from decimal import Decimal, ROUND_HALF_UP

def quadeq(a,b,c):
    disc = b*b - 4*a*c
    # x = -b +- sqrt(disc) / 2a
    offset = math.sqrt(disc) / (2*a)
    return -b/(2*a) - offset, -b/(2*a) + offset

def vol(L,W,x):
    return x * (L - 2*x) * (W - 2*x)

def main():
    for line in stdin:
        L = float(line.split()[0])
        W = float(line.split()[1])
        maximum = 2
        minimum = []
        m, n = (quadeq(12, -4*(L+W), L*W))
        temp1 = vol(L,W,m)
        temp2 = vol(L,W,n)
        maximum = m if temp1>temp2 else n
        minimum.append(0)
        minimum.append(L/2) if L<W else minimum.append(W/2)
        print("%.3f %.3f %.3f"%(maximum,minimum[0], Decimal(str(minimum[1])).quantize(Decimal("0.001"),ROUND_HALF_UP)))

if __name__=="__main__":
    main()
