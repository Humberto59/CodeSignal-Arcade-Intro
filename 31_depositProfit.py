#!/usr/bin/env python
import sys

#31 #Throught the Fog

def depositProfit(deposit, rate, threshold):
    """ Main method """
    result = 0
    mul = float(1) + (float(rate) / float(100))
    tmp = float(deposit)
    while True:
        if tmp >= threshold:
            break
        tmp = tmp * mul
        result += 1 
    return result

def main():
    """ Main flow """
    #a = 100 ; b = 20 ; c = 170
    a = 100 ; b = 1 ; c = 101
    print "Input:  {0}, {1}, {2}".format(a, b, c)
    out = depositProfit(a, b, c)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
