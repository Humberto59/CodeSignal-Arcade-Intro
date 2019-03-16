#!/usr/bin/env python
import sys

#38 #Dark Wilderness

def growingPlant(upSpeed, downSpeed, desiredHeight):
    """ Main method """
    diff = upSpeed - downSpeed
    days = max(1, desiredHeight - downSpeed) / diff
    if ((days * diff) + downSpeed) < desiredHeight:
        days += 1
    return days

def main():
    """ Main flow """
    #a = 100 ; b = 10 ; c = 910
    #a = 10 ; b = 9 ; c = 4
    #a = 5 ; b = 2 ; c = 7
    #a = 7 ; b = 3 ; c = 443
    a = 6 ; b = 5 ; c = 10
    print "Input:  {0}, {1}, {2}".format(a, b ,c)
    out = growingPlant(a, b, c)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
