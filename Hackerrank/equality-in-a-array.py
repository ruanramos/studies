#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    dic = {}
    for i in set(arr):
        dic[i] = arr.count(i)
    
    maximum = max(dic.values())
    num = 0
    for i in dic.items():
        num += i[1]
    
    return num - maximum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
