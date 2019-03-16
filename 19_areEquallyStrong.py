#!/usr/bin/env python
import sys

#19 #Island of Knowledge

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    your_best = yourRight
    if yourLeft > yourRight:
    	your_best = yourLeft

    frend_best = friendsRight
    if friendsLeft > friendsRight:
    	frend_best = friendsLeft

    if your_best == frend_best and \
        (yourLeft + yourRight) == (friendsLeft + friendsRight):
        return True

    return False


def main():
    """ Main flow """
    yL = 10 ; yR = 15 ; fL = 15 ; fR = 10
    print "Input:  {0}, {1}, {2}, {3}".format(yL, yR, fL, fR)
    out = areEquallyStrong(yL, yR, fL, fR)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
