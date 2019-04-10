#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

def combValue(comb):
    a = []
    for i in range(len(comb[0])):
        if comb[0][i] == '1' or comb[1][i] == '1':
            a.append('1')
        else:
            a.append('0')
    return a.count('1')
            

def combValue2(comb):
    num1 = int(comb[0], base=2)
    num2 = int(comb[1], base=2)
    return bin(num1 | num2)[2:].count('1')

# Complete the acmTeam function below.
def acmTeam(topic):
    maxTopics = 0
    peopleMaxTopic = 0
    combinations= itertools.combinations(topic, 2)
    #combinations, combinations2 = itertools.tee(combinations)
    for comb in combinations:
        j = combValue2(comb)
        print(comb, j)
        if j > maxTopics:
            maxTopics = j
    
    #for comb in combinations2:
       # if combValue(comb) == maxTopics:
        #    peopleMaxTopic += 1
    
    return (maxTopics, peopleMaxTopic)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
