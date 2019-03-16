#!/usr/bin/env python
import sys

#58 #Land of Logic

def messageFromBinaryCode(code):
    """ Main method """
    res = list()
    print "len = %d " % len(code)
    for indx in xrange(0, len(code), 8):
        res.append(chr(int(code[indx:indx+8], base=2)))
    return "".join(res)
    """
    return "".join([chr(int(code[8*i:8*i+8],2)) for i in range(len(code)//8)])
    """

def main():
    """ Main flow """
    arg = "010010000110010101101100011011000110111100100001"
    print "Input:  {0}".format(arg)
    out = messageFromBinaryCode(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
