#!/usr/bin/env python
import sys

#32 #Throught the Fog

def absoluteValuesSumMinimization(a):
    """ Main method """
    result = None
    _sum = 0
    for i in range(0, len(a)):
        _sum += a[i]
    _prom = float(_sum)/float(len(a))
    mid = a[len(a)/2]
    diff = abs(a[0] - a[-1]) * len(a) + 1
    print "_sum: {0}, prom: {1}".format(_sum, _prom)
    print "mid: {0}".format(mid)

    _min = int( (len(a) / 2 ) * 0.9)
    _max = int( (len(a) / 2 ) * 1.1) + 1
    for i in range(_min, _max):
        val = a[i]
        _diff = 0
        for j in range(0, len(a)):
            _diff += abs(a[j] - val)

        if _diff < diff:
            diff = _diff
            result = val
            continue
        break

    return result

def main():
    """ Main flow """
    #arg = [2, 4, 7] # 4
    #arg = [1, 1, 3, 4] # 1
    arg = [23] # 23
    #arg = [-10, -10, -10, -10, -10, -9, -9, -9, -8, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50] # 15
    #arg = [-4, -1] # -4
    #arg = [0, 7, 9] # 7
    #arg = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150] # 65
    print "Input:  {0}".format(arg)
    out = absoluteValuesSumMinimization(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
