#!/usr/bin/env python
import sys

#42 #Dark Wilderness

def bishopAndPawn(bishop, pawn):
    """ Main method """
    bis = [ord(bishop[0])-96, int(bishop[1])]
    paw = [ord(pawn[0]) - 96, int(pawn[1])]
    return abs(bis[0] - paw[0]) == abs(bis[1] - paw[1])

def main():
    """ Main flow """
    #a = "a1" ; b = "c3" # Test 1
    a = "h1" ; b = "h3" # Test 2
    print "Input:  {0}, {1}".format(a, b)
    out = bishopAndPawn(a, b)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
