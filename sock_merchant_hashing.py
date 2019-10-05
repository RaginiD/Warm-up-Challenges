#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # dict to store socks color and number of pairs
    socks_data = {}
    for item in ar:
        old_count = socks_data.get(item,0)
        socks_data[item] = old_count+1

    # counter
    count = 0
    for value in socks_data.values():
        count += value//2

    return count

if __name__ == '__main__':

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    print(str(result) + '\n')

