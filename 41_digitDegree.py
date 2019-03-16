#!/usr/bin/env python
import sys

#41 #Dark Wilderness

def digitDegree(a):
    """ Main method """
    result = 0
    while True:
        if len(str(a)) == 1:
            break
        result += 1
        a = sum([int(i) for i in str(a)])
    return result

def main():
    """ Main flow """
    arg = []
    print "Input:  {0}".format(arg)
    out = digitDegree(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
