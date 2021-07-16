# 给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[
# l] = 0。 
# 
#  为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最
# 终结果不会超过 231 - 1 。 
# 
#  例如: 
# 
#  
# 输入:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# 
# 输出:
# 2
# 
# 解释:
# 两个元组如下:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
#  
#  Related Topics 哈希表 二分查找 
#  👍 381 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        s1 = defaultdict(int)
        for n1 in nums1:
            for n2 in nums2:
                s1[n1 + n2] += 1
        s2 = defaultdict(int)
        for n3 in nums3:
            for n4 in nums4:
                s2[n3 + n4] += 1
        count = 0
        for n in s1:
            if -n in s2:
                count += s1[n] * s2[-n]
        return count
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    A = [-1,-1]
    B = [-1,1]
    C =	[-1,1]
    D =	[1,-1]
    print(Solution().fourSumCount(A, B, C, D))