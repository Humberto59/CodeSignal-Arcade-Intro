#!/usr/bin/env python
import sys

#11 #Smooth Sailing

def isLucky(n):
    """ """
    result = False
    nlist = list(str(n))
    h1 = h2 = 0
    for i in range(0, len(nlist) / 2 ):
        h1 += int(nlist[i])
        h2 += int(nlist[-(i + 1)])

    if h1 == h2:
        result = True
    return result

def main():
    """ Main flow """
    num = 1230
    num = 239017
    print isLucky(num)


if __name__ == '__main__':
    sys.exit(main())
