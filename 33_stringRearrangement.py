#!/usr/bin/env python
import sys

#33 #Throught the Fog

def stringRearrangement(inputArray):
    """ Main method """

    for val in inputArray:
        sub_arr = list(inputArray)
        sub_arr.remove(val)
        print "val: {0}, sub_arr: {1}".format(val, sub_arr)
        if search_opts(val, sub_arr) is True:
            return True

    return False

def search_opts(val, array):
    """ search good option for the string rearrangement """
    print "Recursive!"
    print "val: {0}, array: {1}".format(val, array)
    if array == []:
        return True

    opts = list()
    for _str in array:
        if com_str(val,_str) is True:
            opts.append(_str)

    if opts == []:
        return False

    for _str in opts:
        sub_arr = list(array)
        sub_arr.remove(_str)
        res = search_opts(_str, sub_arr)
        if res is True:
            return True
    return False

    """
    for act in range(0, len(inputArray)):
        actual = inputArray[act]
        solution = list([actual])
        print "\nStart with: {0}".format(actual)
        _tmp = list(inputArray)
        _tmp.pop(act)
        indx = 0
        while _tmp:
            target = _tmp[indx]
            if com_str(actual, target) is False:
                if indx == len(_tmp) -1:
                    break
                indx += 1
                continue
            solution.append(target)
            print "Continue with: {0}".format(target)
            actual = target
            _tmp.pop(indx)
            indx = 0

            if len(_tmp) == 0:
                result = True
                break

        if result is True:
            break

    return result
    """

def com_str(str1, str2):
    """ compare strings """
    difs = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            difs += 1
            if difs > 1:
                break
    if difs == 1:
        return True
    return False


def main():
    """ Main flow """
    #arg = ["aba", "bbb", "bab"]
    #arg = ["aa", "ab", "bb"]
    arg = ["abc",  "bef",  "bcc",  "bec",  "bbc",  "bdc"]
    print "Input:  {0}".format(arg)
    out = stringRearrangement(arg)
    print "output: {0}".format(out)


if __name__ == '__main__':
    sys.exit(main())
"""
Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

Note: You're only rearranging the order of the strings, not the order of the letters within the strings!
"""
