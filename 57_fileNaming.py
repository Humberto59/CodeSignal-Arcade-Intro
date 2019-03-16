#!/usr/bin/env python
import sys
import re
from collections import Counter

#57 #Land of Logic

def fileNaming(names):
    """ Main method """
    res = list()
    for indx in xrange(0, len(names)):
        name = names[indx]
        if name not in res:
            res.append(name)
            continue
        name = "%s(%s)" % (name, '%d')
        cnt = 1
        for j in xrange(0, len(res)):
            if name % cnt not in res:
                break
            cnt += 1
        name = name % cnt
        res.append(name)

    return res
    """
    for i in range(len(names)):
        if names[i] in names[:i]:
            j=1
            while names[i]+"("+str(j)+")" in names[:i]:
                j+=1
            names[i]+="("+str(j)+")"
    return names
    """

def main():
    """ Main flow """
    arg = ["doc", "doc", "image", "doc(1)", "doc"] # 1
    arg = ["a(1)",  "a(6)",  "a",  "a",  "a",  "a",  "a",  "a",  "a",  "a",  "a",  "a"] # 2
    print "Input:  {0}".format(arg)
    out = fileNaming(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
