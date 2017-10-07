from sys import stdin, stdout
import math

def testsol(angle, data):
    '''returns 0 if below, 1 if above'''
    d, h, x, n1, n2 = data
    theta1 = math.pi/2 - angle
    theta2 = math.asin( math.sin(theta1) * n2 / n1 )
    x1, x2 = d * math.tan(theta1), h * math.tan(theta2)
    if (x < x1+x2):
        return(0) # undershot
    else:
        return(1) # overshot

def main():
    dataset = [float(x) for x in stdin.readline().split()]
    while(all(dataset)):
        d, h, x, n1, n2 = dataset
        sol = 0
        temp = math.asin(n2/n1) # set at critical angle
        while(temp > 0.00001):
            if testsol(sol,dataset):
                sol -= temp
            else:
                sol += temp
            temp = temp/2
        stdout.write("%.2f\n" % (math.degrees(sol)))
        dataset = [float(x) for x in stdin.readline().split()]

if __name__ == '__main__':
    main()
