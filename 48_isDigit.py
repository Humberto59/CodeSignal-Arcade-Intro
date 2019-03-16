#!/usr/bin/env python
import sys

#48 #Rainbow of Clarity

def isDigit(symbol):
    """ Main method """
    return symbol.isdigit()

def main():
    """ Main flow """
    arg = []
    print "Input:  {0}".format(arg)
    out = isDigit(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
