#!/usr/bin/env python
import sys

#13 #Smooth Sailing

def reverseInParentheses(inputString):
    """ principal method """
    result = None
    list_str = list(inputString)

    while True:
        #print "while: " + "".join(list_str)
        sta_par = None
        end_par = None
        _len = len(list_str)
        j = 0
        for i in range(0, _len):
            j = i
            _val = list_str[i]
            if _val == "(":
                sta_par = i
                continue

            if _val == ")":
                end_par = i
                #print "end_par: " + str(i)
                #print "sta_par: " + str(sta_par)
                diff = i - sta_par - 1
                for j in range(1, (diff/2) + 1):
                    lc = list_str[sta_par + j]
                    rc = list_str[end_par - j]
                    list_str[sta_par + j] = rc
                    list_str[end_par - j] = lc

                #print "tmp0: " + "".join(list_str)
                #raw_input ("swap")
                break

        if end_par != None:
            list_str.pop(end_par)
            list_str.pop(sta_par)

        #print "tmp1: " + "".join(list_str)
        #raw_input("clean")

        if j >= _len:
            break

    return "".join(list_str)

def main():
    """ Main flow """
    #arg = "(bar)"
    arg = "foo(bar(baz))blim"
    #arg = "foo(bar)baz(blim)"
    print "Input:  " + str(arg)
    out = reverseInParentheses(arg)
    print "Output: " + str(out)


if __name__ == '__main__':
    sys.exit(main())
