# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# Complete the bigSorting function below.
def bigSorting(unsorted):
    unsorted.sort()
    print(unsorted)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

