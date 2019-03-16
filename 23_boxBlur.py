#!/usr/bin/env python
import sys

#23 #Rainbow of Clarity

def boxBlur(image):
    """ Main method """
    result = list()
    for i in range(0, len(image) - 2):
        #
        row = image[i]
        prom = list()
        for j in range(0, len(row) - 2):
            res = 0
            res = image[i][j] + image[i][j+1] + image[i][j+2] +\
                image[i+1][j] + image[i+1][j+1] + image[i+1][j+2] +\
                image[i+2][j] + image[i+2][j+1] + image[i+2][j+2]
            res = res / 9
            prom.append(res)

        result.append(prom)
    return result

def main():
    """ Main flow """
    arg = [[1, 1, 1], 
           [1, 7, 1], 
           [1, 1, 1]]
    arg = [[7,  4, 0, 1], 
           [5,  6, 2, 2], 
           [6, 10, 7, 8], 
           [1,  4, 2, 0]]
    print "Input:  {0}".format(arg)
    out = boxBlur(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
