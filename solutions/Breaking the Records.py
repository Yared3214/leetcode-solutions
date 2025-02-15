#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    min = scores[0]
    max = scores[0]
    count_min = 0
    count_max = 0
    for i in range(len(scores)):
        if max < scores[i]:
            max = scores[i]
            count_max += 1
    for j in range(len(scores)):        
        if min > scores[j]:
            min = scores[j]
            count_min += 1
    return [count_max, count_min]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
