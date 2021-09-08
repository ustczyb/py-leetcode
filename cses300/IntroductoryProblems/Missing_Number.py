# Time limit: 1.00 s Memory limit: 512 MB
# You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.
# Input
#
# The first input line contains an integer n.
#
# The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).
#
# Output
#
# Print the missing number.
#
# Constraints
# 2≤n≤2⋅105
# Example
#
# Input:
# 5
# 2 3 1 5
#
# Output:
# 4
import sys
from typing import List

n = -1
or_not = 0
for line in sys.stdin:
    if n == -1:
        n = int(line)
        for i in range(1, n + 1):
            or_not ^= i
    else:
        nums = line.split(' ')
        for num_str in nums:
            or_not ^= int(num_str)
print(or_not)
