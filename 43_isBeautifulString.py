#!/usr/bin/env python
import sys

#43 #Eruption of Light

def isBeautifulString(inStr):
    """ Main method """
    result = None
    cnt_li = list([0]*26)
    for indx in xrange(0, len(inStr)):
        cnt_li[ord(inStr[indx])-97] += 1

    cnt = cnt_li[0]
    for indx in xrange(1, 26):
        cnt += cnt_li[indx]
        if cnt_li[indx] <= cnt_li[indx-1]:
            continue
        return False

    return True

def main():
    """ Main flow """
    arg = "bbbaacdafe"
    print "Input:  {0}".format(arg)
    out = isBeautifulString(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
