#!/usr/bin/env python
import sys

#35 #Driving Deeper
import re
def firstDigit(arg):
    """ Main method """
    return re.findall(r'\d', arg)[0]

def main():
    """ Main flow """
    arg = "var_1__Int"
    print "Input:  {0}".format(arg)
    out = firstDigit(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
