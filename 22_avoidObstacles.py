#!/usr/bin/env python
import sys

#22 #Island of Knowledge

def avoidObstacles(inputArray):
    """ Main method """
    result = 0
    cnt_li = list([False]*1001)
    sort_li = list()

    for val in inputArray:
        cnt_li[val] = True

    for i in range(0, len(cnt_li)):
        if cnt_li[i] is False:
            continue

        sort_li.append(i)

        if len(sort_li) == len(inputArray):
            break

    print "Sorted: " + str(sort_li)

    for base in range(2, 1002):
        #print "Cheking: " + str(base)
        #raw_input()
        mul = 0
        li = 0
        stg = 0
        while True:
            mul += 1
            num = base * mul
            if li > len(sort_li) - 1:
                result = base
                break

            val = sort_li[li]
            #print "num: '%d', val: '%d'" % (num, val)
            if num == val:
                break

            if num < val:
                continue

            if num > val:
                li += 1
                mul -= 1
                continue

        if result != 0 :
            break

    return result


def main():
    """ Main flow """
    #arg = [1, 2, 3, 4, 99, 5, 6]
    #arg = [5, 3, 6, 7, 9]
    #arg = [2, 3]
    #arg = [1, 4, 10, 6, 2]
    #arg = [1000, 999]
    arg = [19, 32, 11, 23]
    print "Input:  " + str(arg)
    out = avoidObstacles(arg)
    print "output: " + str(out)


if __name__ == '__main__':
    sys.exit(main())
