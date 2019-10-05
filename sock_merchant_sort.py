#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    i = 0
    # counter
    count = 0
    # sort the array
    ar.sort()
    while i < n and i+1 < n:
        if ar[i] == ar[i+1]:
            count += 1
            i+=2
        else:
            i+=1
    return count

if __name__ == '__main__':

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    print(str(result) + '\n')

