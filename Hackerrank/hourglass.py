#!/bin/python3

import math
import os
import random
import re
import sys

def sumHourglass(matrix, i, j):
    return matrix[i][j] + matrix[i-1][j+1] + matrix[i-1][j] + matrix[i-1][j-1] + matrix[i+1][j-1] + matrix[i+1][j] + matrix[i+1][j+1] 

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    bigger = -125192851298
    for i in range(1, len(arr) - 1):
        for j in range(1, len(arr) - 1):
            if sumHourglass(arr, i, j) > bigger:
                bigger = sumHourglass(arr, i, j)
    print(bigger)
