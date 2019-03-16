#!/usr/bin/env python
import sys

#44 #Eruption of Light

def findEmailDomain(address):
    """ Main method """
    return address.split('@')[-1]


def main():
    """ Main flow """
    arg = []
    print "Input:  {0}".format(arg)
    out = findEmailDomain(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
