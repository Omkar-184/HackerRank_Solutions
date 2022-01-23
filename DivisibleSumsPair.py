
import math
import os
import random
import re
import sys





def divisibleSumPairs(n, k, ar):
    count=0
    for i in range(n-1):
        # for j in range(i+1, n):
        j = i+1
        while j<n:
            if (ar[i] + ar[j] )%k == 0 :
                print(ar[i])
                print(ar[j])
                count += 1
                # i+=1
            j+=1
    # print(count)
    return count


first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])
ar = list(map(int, input().rstrip().split()))
result = divisibleSumPairs(n, k, ar)
