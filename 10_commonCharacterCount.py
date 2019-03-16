#!/usr/bin/env python
import sys

#10 #Smooth Sailing

def commonCharacterCount(s1, s2):
    """ """
    result = 0
    compared = list()
    str2 = list(s2)
    for i1 in range(0, len(s1)):

        for i2 in range(0, len(str2)):
            if s1[i1] == str2[i2]:
                result += 1
                str2.pop(i2)
                break

    return result

def main():
    """ Main flow """
    s1 = "aabcc" ; s2 = "adcaa"
    print commonCharacterCount(s1, s2)


if __name__ == '__main__':
    sys.exit(main())
