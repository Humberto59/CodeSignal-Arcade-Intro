#!/usr/bin/env python
import sys

#25 #Rains of Reason

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    """ Main method """
    result = None
    for i in range(0, len(inputArray)):
        val = inputArray[i]
        if val == elemToReplace:
            inputArray[i] = substitutionElem

    return inputArray

def main():
    """ Main flow """
    arg = [1, 2, 1] ; v1 = 1 ; v2 = 3
    print "Input: {0}, {1}, {2} ".format(arg, v1, v2)
    out = arrayReplace(arg, v1, v2)
    print "output: " + str(out)


if __name__ == '__main__':
    sys.exit(main())
