#!/usr/bin/env python
import sys

#49 #Rainbow of Clarity

def lineEncoding(inStr):
    """ Main method """
    result = list()
    cnt = 1
    act = inStr[0]
    inStr = inStr + "%"
    for indx in xrange(1, len(inStr)):
        char = inStr[indx]
        if act == char:
            cnt += 1
            continue
        result.append("{0}{1}".format(cnt if cnt > 1 else "", act))
        act = char
        cnt = 1
    return "".join(result)

def main():
    """ Main flow """
    arg = "aabbbc"
    print "Input:  {0}".format(arg)
    out = lineEncoding(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
