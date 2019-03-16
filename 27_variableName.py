#!/usr/bin/env python
import sys
import re

#27 #Rains of Reason

def variableName(name):
    """ Main method """
    if re.match('^[0-9]' ,name):
        print "1"
        return False
    if  re.match('^[A-Za-z_0-9]+$', name) is None:
        print "2"
        return False
    return True

def main():
    """ Main flow """
    arg = "var_1__Int"
    #arg = "qq-q"
    print "Input:  {0}".format(arg)
    out = variableName(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
