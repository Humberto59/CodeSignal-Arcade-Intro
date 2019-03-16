#!/usr/bin/env python
import sys

#16 #Exploring the Waters

def areSimilar(a, b):
    """ Main method """
    swap = list()
    miss = 0
    for i in range(0, len(a)):
        if a[i] == b[i]:
            continue
        miss += 1
        swap.append(i)
        if miss > 2:
            return False

    if miss != 0:
        s2 = swap.pop()
        s1 = swap.pop()

        if a[s1] != b[s2] or a[s2] != b[s1]:
            return False

    return True

def main():
    """ Main flow """
    a = [1, 2, 3]; b = [1, 2, 3]
    #a = [1, 2, 3]; b = [2, 1, 1]
    print "Input:  " + str(a) + ", " + str(b)
    out = areSimilar(a, b)
    print "output: " + str(out)


if __name__ == '__main__':
    sys.exit(main())
