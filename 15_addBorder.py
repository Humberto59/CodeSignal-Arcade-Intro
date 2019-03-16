#!/usr/bin/env python
import sys

#15 #Exploring the Waters

def addBorder(picture):
    """ Main method """
    result = list()

    _len = len(picture[0])
    result.append("*" * (_len+2))

    for i in range(0, len(picture)):
        result.append("*{0}*".format(picture[i]))

    result.append("*" * (_len+2))
    return result

def main():
    """ Main flow """
    arg = ["abc", "ded"]
    print "Input:  " + str(arg)
    out = addBorder(arg)
    print "output: " + str(out)


if __name__ == '__main__':
    sys.exit(main())
