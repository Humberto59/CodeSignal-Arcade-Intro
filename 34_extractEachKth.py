#!/usr/bin/env python
import sys

#3X #Driving Deeper

def extractEachKth(inputArray, k):
    """ Main method """
    res = list()
    for indx in range(0, len(inputArray)):
        if (indx % k ) != 0:
            res.append(inputArray[indx])
    return  res

def main():
    """ Main flow """
    arg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ; k = 3
    #arg = [1, 1, 1, 1, 1] ; k =1
    #arg = [2, 4, 6, 8, 10] ; k = 2
    print "Input:  {0}, {1}".format(arg, k)
    out = extractEachKth(arg, k)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
