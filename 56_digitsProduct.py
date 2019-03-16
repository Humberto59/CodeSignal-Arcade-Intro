#!/usr/bin/env python
import sys

#56 #Land of Logic

def digitsProduct(product):
    """ Main method """
    res = list()
    tmp = product
    if product == 0:
        return 10
    if product < 10:
        return product
    while True:
        if tmp == 1 :
            break
        for mod in xrange(9, 1, -1):
            if tmp % mod == 0 or \
                (tmp < 10 and tmp % mod == 1):
                res.insert(0, mod)
                tmp = tmp / mod
                break
        #else:
        #    return -1
        print "mod %d, tmp %d" % (mod, tmp)
        if mod == 2 :
            #and (not res or res[-1] != 2):
            break
    print "res " + str(res)
    return int("".join(map(str,res))) if len(res) > 1 else -1
    #return int("".join(map(str,res)))

def main():
    """ Main flow """
    #arg = 12 # 1
    #arg = 19 # 2
    #arg = 450 # 3
    arg = 598 # ?
    #arg = 22 # ?
    print "Input:  {0}".format(arg)
    out = digitsProduct(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
"""
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.
"""
