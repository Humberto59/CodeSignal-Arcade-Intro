#!/usr/bin/env python
import sys
import collections

#46 #Eruption of Light

def electionWinners(votes, k):
    """ Main method """
    _max = max(votes)
    if k == 0:
        if collections.Counter(votes)[_max] == 1:
            return 1
        return 0
    res = 0
    for cand in votes:
        if cand + k > _max:
            res += 1
    return res
    """
    _max = max(votes)
    return int(collections.Counter(votes)[_max] == 1) if k == 0 else \
            sum([num + k > _max for num in votes])
    """

def main():
    """ Main flow """
    arg = [2, 3, 5, 2] ; k = 3 # Test 1
    arg = [5, 3, 2, 1] ; k = 0 # Test 4
    print "Input:  {0}, {1}".format(arg, k)
    out = electionWinners(arg, k)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
