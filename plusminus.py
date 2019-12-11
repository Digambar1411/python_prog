

import math
# import os
# import random
# import re
# import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    szero=0
    spos=0
    sneg=0
    for i in range(n):
        if arr[i]<0:
            sneg+=1
        elif arr[i]>0:
            spos+=1
        else:
            szero+=1
    a=spos/n
    b=sneg/n
    c=szero/n
    
    a="{0:.6f}".format(a)
    b="{0:.6f}".format(b)
    c="{0:.6f}".format(c)
    print(a)
    print(b)
    print(c)
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
