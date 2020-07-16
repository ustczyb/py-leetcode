# 在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。 
# 
#  示例: 
# 
#  输入: 
# 
# 1 0 1 0 1
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
#   dp[m][n] = dp[m - 1][n] dp[m][n - 1] dp[m - 1][n - 1]
# 
# 输出: 4 
#  Related Topics 动态规划

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        max_size = 0
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        if matrix[0][0] == '1':
            dp[0][0] = 1
            if max_size < 1:
                max_size = 1
        for i in range(1, len(matrix[0])):
            if matrix[0][i] == '0':
                dp[0][i] = 0
            else:
                dp[0][i] = 1
                if max_size < 1:
                    max_size = 1
        for i in range(1, len(matrix)):
            if matrix[i][0] == '0':
                dp[i][0] = 0
            else:
                dp[i][0] = 1
                if max_size < 1:
                    max_size = 1
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '0':
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                    if max_size < dp[i][j]:
                        max_size = dp[i][j]
        return max_size * max_size



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    matrix = [["1","0","1","0"],
              ["1","0","1","1"],
              ["1","0","1","1"],
              ["1","1","1","1"]]
    print(Solution().maximalSquare(matrix))
