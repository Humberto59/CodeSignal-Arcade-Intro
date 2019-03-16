#!/usr/bin/env python
import sys

#39 #Dark Wilderness

def knapsackLight(v1, w1, v2, w2, mw):
    """ value1, weight1, value2, weight2, maxWeight """
    #return max(int(w1<=W)*v1, int(w2<=W)*v2, int(w1+w2<=W)*(v1+v2))
    if mw < w1 and mw < w2:
        return 0
    if mw >= w1 + w2:
        return v1 + v2
    if (v1 > v2 and w1 <= mw) or w2 > mw:
        return v1
    return v2
def main():
    """ Main flow """
    v1 = 10 ; w1 = 5 ; v2 = 6 ; w2 = 4 ; mw = 8
    print "Input:  {0}, {1}, {2}, {3}, {4}".format(v1, w1, v2, w2, mw)
    out = knapsackLight(v1, w1, v2, w2, mw)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
