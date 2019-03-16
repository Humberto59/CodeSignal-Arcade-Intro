#!/usr/bin/env python
import sys

#3X #Throught the Fog

def circleOfNumbers(n, firstNumber):
    """ Main method """
    result = ( firstNumber + (n / 2) ) % n
    return result

def main():
    """ Main flow """
    a = 10; b = 2
    a = 10; b = 7
    a = 4 ; b = 1
    print "Input:  {0}, {1}".format(a, b)
    out = circleOfNumbers(a, b)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
