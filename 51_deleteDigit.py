#!/usr/bin/env python
import sys

#50 #Rainbow of Clarity

def deleteDigit(n):
    """ Main method """
    nli = list(str(n))
    _li = list()
    for i in nli:
        tmp = list(nli)
        tmp.remove(i)
        _li.append(int("".join(tmp)))
    return max(_li)
    #max([int("".join(list(nli).remove(i))) for i in nli])
    """
    n = str(n)
    return max(int(''.join(n[:i]+n[i+1:])) for i in range(len(n)))
    """

def main():
    """ Main flow """
    arg = 152 # Test 1
    arg = 222250 # Test 6
    print "Input:  {0}".format(arg)
    out = deleteDigit(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
