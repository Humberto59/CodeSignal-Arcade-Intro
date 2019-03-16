#!/usr/bin/env python
import sys

#26 #Rains of Reason

def evenDigitsOnly(n):
    """ Main method """
    n_li = list(str(n))
    for index in range(0, len(n_li)):
        if int(n_li[index]) % 2 != 0:
            return False
    return True

def main():
    """ Main flow """
    arg = 248622
    print "Input:  {0}".format(arg)
    out = evenDigitsOnly(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
