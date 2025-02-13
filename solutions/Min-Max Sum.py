#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    total_sum = 0
    max_val = max(arr)
    min_val = min(arr)
    for x in arr:
        total_sum += x
    max_sum = total_sum - min_val
    min_sum = total_sum - max_val
    
    print (min_sum, max_sum)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
