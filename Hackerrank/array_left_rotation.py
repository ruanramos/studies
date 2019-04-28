#!/bin/python3

import math
import os
import random
import re
import sys

def rotate_smart(arr, d):
    end = arr[0:d]
    start = arr[d:]
    return start + end


if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    for i in rotate_smart(a, d):
        print(i, end = ' ')