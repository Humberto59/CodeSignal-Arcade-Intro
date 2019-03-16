#!/usr/bin/env python
import sys

#53 #Land of Logic

def validTime(time):
    """ Main method """
    _hh, _mm = time.split(":")
    return 0 <= int(_hh) <= 23 and 0 <= int(_mm) <= 59

def main():
    """ Main flow """
    arg = "24:00" # Test 4
    print "Input:  {0}".format(arg)
    out = validTime(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
