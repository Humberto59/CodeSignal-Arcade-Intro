#!/usr/bin/env python
import sys

#52 #Land of Logic

import re
def longestWord(text):
    """ Main method """
    result = None
    words = re.findall('[a-zA-Z]+', text)
    _max = 0
    for word in words:
        _len = len(word)
        if _len < _max:
            continue
        _max = _len
        result = word
    return result
    """
    return max(re.split('[^a-zA-Z]', text), key=len)
    """

def main():
    """ Main flow """
    #arg = "Ready, steady, go!" # Test 1
    arg = "Ready[[[, steady, go!" # Test 2
    print "Input:  {0}".format(arg)
    out = longestWord(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
