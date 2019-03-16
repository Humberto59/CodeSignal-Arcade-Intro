#!/usr/bin/env python
import sys

#12 #Smooth Sailing

def sortByHeight(a):
    """ """
    result = list()
    trees = list()
    people = list()
    _people = list([0] * 1001)
    org_len = len(a)

    for i in range(0, org_len):
        height = a[i]
        if height == -1:
            trees.append(i)
            continue

        _people[height] += 1

    #print "trees: " + str(trees)
    for i in range(0, len(_people)):
        if _people[i] == 0:
            continue
        rep = _people[i]
        for j in range(0, rep):
            people.append(i)
        #print "_people i: {0}, rep {1} ".format(i, _people[i])

    #print "people: " + str(people)
    #sys.exit(1)

    for i in range(0, org_len):
        if trees and trees[0] == i:
            result.append(-1)
            trees.pop(0)
            continue

        result.append(people.pop(0))

    return result

def main():
    """ Main flow """
    _list = [-1, 150, 190, 170, -1, -1, 160, 180]
    print sortByHeight(_list)


if __name__ == '__main__':
    sys.exit(main())
