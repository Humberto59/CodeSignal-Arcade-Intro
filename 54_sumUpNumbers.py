#!/usr/bin/env python
import sys

#54 #Land of Logic
import re
def sumUpNumbers(inputString):
    """ Main method """
    return sum(map(int, re.findall('[0-9]+', inputString))) 

def main():
    """ Main flow """
    arg = "2 apples, 12 oranges"
    print "Input:  {0}".format(arg)
    out = sumUpNumbers(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
