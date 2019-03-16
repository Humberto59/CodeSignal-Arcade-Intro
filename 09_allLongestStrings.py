#!/usr/bin/env python
import sys

#9 #Smooth Sailing

def allLongestStrings(inputArray):
    """ """
    result = list()
    max_len = 0
    for _str in inputArray:
        _len = len(_str)
        if _len > max_len:
            max_len = _len
            result = [_str]
            continue
        if _len == max_len:
            result.append(_str)
            continue

    return result

def main():
    """ Main flow """
    #_list = [1, 2, 3, 4, 99, 5, 6]
    _list = ["aba", "aa", "ad", "vcd", "aba"]
    print allLongestStrings(_list)


if __name__ == '__main__':
    sys.exit(main())
