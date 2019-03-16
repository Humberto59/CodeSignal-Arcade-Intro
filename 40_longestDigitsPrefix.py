#!/usr/bin/env python
import sys

#40 #Dark Wilderness
import re
def longestDigitsPrefix(a):
    return re.findall("^\d*", a)[0]

def main():
    """ Main flow """
    arg = "123aa1"
    arg = " 3) always check for whitespaces"
    print "Input:  '{0}'".format(arg)
    out = longestDigitsPrefix(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
