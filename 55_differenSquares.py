#!/usr/bin/env python
import sys

#55 #Land of Logic

def differenSquares(matrix):
    """ Main method """
    res = set()
    for h in xrange(0, len(matrix) - 1):
        for w in xrange(0,len(matrix[h]) - 1):
            res.add((matrix[h][w], matrix[h][w+1], matrix[h+1][w], matrix[h+1][w+1]))
    return len(res)

def main():
    """ Main flow """
    arg = [[1, 2, 1],
           [2, 2, 2],
           [2, 2, 2],
           [1, 2, 3],
           [2, 2, 1]]
    print "Input:  {0}".format(arg)
    out = differenSquares(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
