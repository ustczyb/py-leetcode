# 给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。 
# 
#  示例 1: 
# 
#  输入: n = 12
# 输出: 3 
# 解释: 12 = 4 + 4 + 4. 
# 
#  示例 2: 
# 
#  输入: n = 13
# 输出: 2
# 解释: 13 = 4 + 9. 
#  Related Topics 广度优先搜索 数学 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
from math import sqrt


class Solution:

    def numSquares(self, n: int) -> int:
        arr = [-1] * (n + 1)
        i = 0
        while True:
            s = i * i
            if s > n:
                break
            arr[i * i] = 1
            i += 1
        if arr[n] != -1:
            return arr[n]
        for j in range(1, i):
            for k in range(j * j + 1, min((j + 1) * (j + 1), n + 1)):
                arr[k] = min(arr[k - l * l] + 1 for l in range(1, j + 1))
        return arr[n]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().numSquares(13))
