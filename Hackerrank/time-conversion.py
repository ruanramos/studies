#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(S):
    #
    # Write your code here.
    #
    hour = int(S[:2])
    minutes = S[3:5]
    seconds = S[6:8]
    letters = S[-2:] #pm or am

    if letters == 'AM':
        if hour == 12:
            return '{0}:{1}:{2}'.format(str(hour-12).zfill(2), minutes.zfill(2), seconds.zfill(2))
        else:
            return '{0}:{1}:{2}'.format(str(hour).zfill(2), minutes.zfill(2), seconds.zfill(2))
    if letters == 'PM':
        if hour == 12:
            return '{0}:{1}:{2}'.format(str(hour).zfill(2), minutes.zfill(2), seconds.zfill(2))
        return '{0}:{1}:{2}'.format(str((hour + 12)%24).zfill(2), minutes.zfill(2), seconds.zfill(2))

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()

