#!/usr/bin/env python
import sys

#7 #Edge of the Ocean

def almostIncreasingSequence(sequence):
    """ Method """

    result = True
    need_rm = False
    last_fail = False

    for i in range(1, len(sequence)):
        if sequence[i-1] >= sequence[i]:
            if need_rm is False:
                need_rm = True
                last_fail = True
                continue
            return False

        if need_rm is True and \
           last_fail is True :

               if sequence[i-2] > sequence[i] and i == 2:
                       continue

               if sequence[i-2] >= sequence[i] and\
                   i >= 3 and sequence[i-3] >= sequence[i-1]:
                   return False

        last_fail = False

    return result


def main():
    """ Main flow """
    #_list = [5, 4, 6]
    #_list = [1, 2, 1, 2]
    #_list = [4, 5, 6, 1, 2, 3]
    #_list = [1, 2, 5, 3, 5]
    #_list = [10, 1, 2, 3, 4, 5]
    #_list = [1, 2, 3, 4, 5, 3, 5, 6]
    _list = [1, 2, 3, 4, 99, 5, 6]
    print almostIncreasingSequence(_list)


if __name__ == '__main__':
    sys.exit(main())
