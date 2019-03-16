#!/usr/bin/env python
import sys

#50 #Rainbow of Clarity

def chessKnight(cell):
    """ Main method """
    x, y = ord(cell[0])-96, int(cell[1])
    res = 0
    for mul2 in [-2, 2]:
        for mul1 in [-1, 1]:
            res += int( 1 <= x + mul2 <= 8 and 1 <= y + mul1 <= 8)
            res += int( 1 <= x + mul1 <= 8 and 1 <= y + mul2 <= 8)
    return res

def main():
    """ Main flow """
    arg = "a1"
    print "Input:  {0}".format(arg)
    out = chessKnight(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
