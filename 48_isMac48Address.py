#!/usr/bin/env python
import sys
import re

#48 #Eruption of Light

def isMac48Address(inStr):
    """ Main method """
    if len(re.findall('-',inStr)) != 5:
        return False
    return (len(re.findall('[0-9]|[A-F]|-', inStr)) == 17)

def main():
    """ Main flow """
    arg = "00-1B-63-84-45-E6" # Test 1
    #arg = "Z1-1B-63-84-45-E6" # Test 2
    #arg = "not a MAC-48 address" # Test 3
    print "Input:  {0}".format(arg)
    out = isMac48Address(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
