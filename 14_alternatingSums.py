#!/usr/bin/env python
import sys

#14 #Exploring the Waters

def alternatingSums(a):
    """ Main method """
    result = None
    t1 = 0
    t2 = 0
    for i in range(0, len(a), 2):
        t1 += a[i]
        if i+1  <= len(a) - 1:
            t2 += a[i+1]
    return [t1, t2]

def main():
    """ Main flow """
    arg = [1, 2, 3, 4, 99, 5, 6]
    arg = [50, 60, 60, 45, 70]
    print "Input:  " + str(arg)
    out = alternatingSums(arg)
    print "output: " + str(out)


if __name__ == '__main__':
    sys.exit(main())
