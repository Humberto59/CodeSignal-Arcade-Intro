#!/usr/bin/env python
import sys

#8 #Edge of the Ocean

def matrixElementstsSum(matrix):
    """ """
    result = 0
    ign_col = list()
    # Row
    for row in range(0, len(matrix)):
        # Col
        for col in range(0, len(matrix[row])):
            val = matrix[row][col]
            #print "Row: %i, Col %i, Val: %i" % (row, col, val)
            if col in ign_col:
                continue

            if val == 0:
                ign_col.append(col)
                continue

            result += val


    return result

def main():
    """ Main flow """
    matrix = [[0, 1, 1, 2],
              [0, 5, 0, 0],
              [2, 0, 3, 3]]

    print matrixElementstsSum(matrix)


if __name__ == '__main__':
    sys.exit(main())
