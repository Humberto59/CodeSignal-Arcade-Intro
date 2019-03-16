#!/usr/bin/env python
import sys

#60 #Land of Logic

def sudoku(grid):
    """ Main method """
    for indx in xrange(0,9):
        row = sum(set(grid[indx]))
        col = sum(set([ grid[j][indx] for j in xrange(0, 9) ]))
        print "indx %d, row %d, col %d" % (indx, row, col)
        if col != 45 or row != 45:
            return False
    for row in xrange(0, 9, 3):
        for col in xrange(0, 9, 3):
            tmp = sum(set(grid[row][col:col+3] + grid[row+1][col:col+3] + grid[row+2][col:col+3]))
            print "tmp %d" % tmp
            if tmp != 45:
                return False
    return True

def main():
    """ Main flow """
    arg = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
           [4, 6, 5, 8, 7, 9, 3, 2, 1],
           [7, 9, 8, 2, 1, 3, 6, 5, 4],
           [9, 2, 1, 4, 3, 5, 8, 7, 6],
           [3, 5, 4, 7, 6, 8, 2, 1, 9],
           [6, 8, 7, 1, 9, 2, 5, 4, 3],
           [5, 7, 6, 9, 8, 1, 4, 3, 2],
           [2, 4, 3, 6, 5, 7, 1, 9, 8],
           [8, 1, 9, 3, 2, 4, 7, 6, 5]] # 1
    print "Input:  "#{0}".format(arg)
    for row in arg:
        print row
    out = sudoku(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
