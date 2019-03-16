#!/usr/bin/env python
import sys

#6 #Edge of the Ocean

def makeArrayConsecutive2(statues):

    lcount = list([False] * 10)
    for _num in statues:
        if lcount[_num] is True:
            continue
        lcount[_num] = True

    print "Booleand count array: " + str(lcount)

    lsort = list()
    for i in range(0, len(lcount)):
        _val = lcount[i]
        if _val is True:
            lsort.append(i)

    print "Sorted list: " + str(lsort)

    result = 0
    for i in range(1, len(lsort)):
        result += (lsort[i] - lsort[i-1]) - 1

    print "Result: " + str(result)

    return result


def main():
    """ Main flow """
    _list = [6, 2, 3, 8]
    #_list = [3, 0]
    #_list = [5, 4, 6]
    #_list = [1]
    _list = [1, 3, 5, 3, 1]
    makeArrayConsecutive2(_list)


if __name__ == '__main__':
    sys.exit(main())
