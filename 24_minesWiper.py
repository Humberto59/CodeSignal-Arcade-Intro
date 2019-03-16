#!/usr/bin/env python
import sys

#23 #Rainbow of Clarity

def minesWiper(a):
    """ Main method """
    result = list()
    for i in range(0, len(matrix)):
        #
        row = list()
        for j in range(0, len(matrix[i])):
            #
            val = 0
            for _i in range(-1, 2):
                for _j in range(-1, 2):
                    if _i == 0 and _j == 0:
                        continue
                    if i + _i < 0 or i + _i >= len(matrix):
                        continue
                    if j + _j < 0 or j + _j >= len(matrix[i]):
                        continue

                    if matrix[i+_i][j+_j] is False:
                        continue
                    val += 1
            row.append(val)
        result.append(row)

    return result

def main():
    """ Main flow """
    arg = []
    print "Input:  {0}".format(arg)
    out = minesWiper(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
