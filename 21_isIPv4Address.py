#!/usr/bin/env python
import sys

#21 #Island of Knowledge

def isIPv4Address(inputString):
    """ Main method """
    num_li = inputString.split('.')
    if len(num_li) != 4:
        print "ret 1"
    	return False

    for i in range(0, 4):
    	val = num_li[i]
    	if val == "" or not val.isdigit():
                print "ret 2"
    		return False

    	val = int(val)
        
    	if val < 0 or val > 255:
                print "ret 3"
    		return  False
    return True

def main():
    """ Main flow """
    arg = "172.16.254.1"
    print "Input:  " + str(arg)
    out = isIPv4Address(arg)
    print "output: " + str(out)


if __name__ == '__main__':
    sys.exit(main())
