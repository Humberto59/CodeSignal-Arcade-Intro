#!/usr/bin/env python
import sys

#17 #Exploring the Waters

def arrayChange(inputArray):
    """ Main method """
    result = 0
    for i in range(0, len(inputArray) - 1):
        if inputArray[i] < inputArray[i+1]:
            continue
        upd = (inputArray[i] - inputArray[i+1]) + 1
        inputArray[i+1] += upd
        result += upd
    return result

def main():
    """ Main flow """
    arg = [1, 1, 1]
    print "Input:  " + str(arg)
    out = arrayChange(arg)
    print "output: " + str(out)


if __name__ == '__main__':
    sys.exit(main())
