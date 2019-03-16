#!/usr/bin/env python
import sys

#59 #Land of Logic

def spiralNumbers(n):
    """ Main method """
    res = [[0 for _ in xrange(n)] for _ in xrange(n)]
    cnt = 1
    for indx in xrange(0, n / 2 + n % 2):
        print "--- indx %d ---" % indx
        # From left to right
        for j in xrange(indx, n-indx):
            print "1 res[%d][%d] = %d" % (indx, j, cnt)
            res[indx][j] = cnt ; cnt += 1
        # From top to botton
        for j in xrange(indx+1, n-indx):
            print "2 res[%d][%d] = %d" % (j, n-1-indx, cnt)
            res[j][n-1-indx] = cnt ; cnt += 1
        # From righ to left
        for j in xrange(n-indx-2, indx, -1):
            print "3 res[%d][%d] = %d" % (n-1-indx, j, cnt)
            res[n-1-indx][j] = cnt ; cnt += 1
        # From botton to top
        for j in xrange(n-indx-1, indx , -1):
            print "4 res[%d][%d] = %d" % (j, indx, cnt)
            res[j][indx] = cnt ; cnt += 1
    return res

def main():
    """ Main flow """
    arg = 3
    print "Input:  {0}".format(arg)
    out = spiralNumbers(arg)
    print "output: "
    for arr in out:
        print str(arr)


if __name__ == '__main__':
    sys.exit(main())
