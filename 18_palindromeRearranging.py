#!/usr/bin/env python
import sys

#18 #Emploring the Waters

def palindromeRearranging(inputString):
    """ Main method """
    li_str = list(inputString)
    count = list()
    for i in range(0, len(li_str)):
        cha = li_str[i]
        if cha in count:
            count.remove(cha)
            continue
        count.append(cha)

    str_mod = len(li_str) % 2
    cnt_mod = len(count)

    if str_mod == cnt_mod:
        return True
    return False

def main():
    """ Main flow """
    arg = []
    print "Input:  {0}".format(arg)
    out = palindromeRearranging(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
