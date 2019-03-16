#!/usr/bin/env python
import sys

#20 #Rainbow of Clarity

def arrayMaximalAdjacentDifference(inputArray):
    """ Main method """
    result = 0
    for i in range(0, len(inputArray) - 1):
	dif = abs(inputArray[i] - inputArray[i+1])
	if dif > result:
		result = dif
    return result

def main():
    """ Main flow """
    arg = [2, 4, 1, 0]
    print "Input:  {0}".format(arg)
    out = arrayMaximalAdjacentDifference(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
