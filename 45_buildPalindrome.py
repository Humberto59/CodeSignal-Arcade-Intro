#!/usr/bin/env python
import sys

#45 #Eruption of Light

def buildPalindrome(st):
    """ Main method """
    for indx in xrange(2, len(st)):
        c0 = indx-2
        c1 = indx-1
        c2 = indx
        print "indx = %d" % indx
        if st[c0] == st[c2]:
            if checkPal(c0, c2, st) is False:
                continue
            c1 = c0
            break
        elif st[c1] == st[c2]:
            if checkPal(c1, c2, st) is False:
                continue
            break
        c1 = c2
    added = len(st) - (c2 + 1)
    res = list(st)
    print "added " + str(added) 
    for indx in xrange(1, (c1 + 1) - added):
        res.append(st[c1 - indx - added])

    return "".join(res)

def checkPal(c0,c1, inStr):
    print "Here could be a Palindrome: {0}({1}), {2}({3})".format(\
            c0, inStr[c0], c1, inStr[c1])
    if c1 == len(inStr):
        print "True 0"
        return True
    if (len(inStr) - 1 - c1) > c0 :
        print "False 0"
        return False
    for i in xrange(c1, len(inStr)):
        dif = i - c1
        if inStr[c0 - dif] != inStr[c1 + dif]:
            print "False 1"
            return False
    print "True 1"
    return True


def main():
    """ Main flow """
    #arg = "abcdc" # Test 1
    #arg = "ababab" # Test 2
    #arg = "abba" # Test 3
    #arg = "abaa" # Test 4
    #arg = "abc" # Test 6
    arg = "aaaaaaaaa" # Test 21
    print "Input:  {0}".format(arg)
    out = buildPalindrome(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
