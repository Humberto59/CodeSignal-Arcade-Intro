#!/usr/bin/env python
import sys

#28 #Rains of Reason

def alphabeticShift(inputString):
    """ Main method """
    result = list()
    for i in list(inputString):
        result.append(chr( (((ord(i) - 96) % 26) + 97)  ))
    return "".join(result)

def main():
    """ Main flow """
    arg = "crazy"
    print "Input:  {0}".format(arg)
    out = alphabeticShift(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
