#!/usr/bin/env python
import sys

#36 #Driving Deeper

def differentSymbolsNative(s):
    """ Main method """
    result = 0
    _cnt = list([False]*26)
    for char in list(s):
        _cnt[ord(char) - 97] = True
    for val in _cnt:
        if val is True:
            result += 1
    return result

    #return len(set(s))

def main():
    """ Main flow """
    arg = "cabca"
    print "Input:  {0}".format(arg)
    out = differentSymbolsNative(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
