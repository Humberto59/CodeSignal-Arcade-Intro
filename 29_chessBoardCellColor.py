#!/usr/bin/env python
import sys

#29 #Rains of Reason

def chessBoardCellColor(cell1, cell2):
    """ Main method """
    c1_x = ord(cell1[0]) - 64
    c1_y = int(cell1[1])
    c2_x = ord(cell2[0]) - 64
    c2_y = int(cell2[1])

    if ((c1_x + c1_y) % 2) != ((c2_x + c2_y) % 2):
        return False

    return True

def main():
    """ Main flow """
    #arg = "A1" ; arg1 = "C3"
    arg = "A1" ; arg1 = "H3"
    print "Input:  {0}, {1}".format(arg, arg1)
    out = chessBoardCellColor(arg, arg1)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
