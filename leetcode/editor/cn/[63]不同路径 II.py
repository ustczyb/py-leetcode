# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。 
# 
#  机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。 
# 
#  现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？ 
# 
#  
# 
#  网格中的障碍物和空位置分别用 1 和 0 来表示。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# 输出：2
# 解释：
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
#  
# 
#  示例 2： 
# 
#  
# 输入：obstacleGrid = [[0,1],[0,0]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == obstacleGrid.length 
#  n == obstacleGrid[i].length 
#  1 <= m, n <= 100 
#  obstacleGrid[i][j] 为 0 或 1 
#  
#  Related Topics 数组 动态规划 
#  👍 535 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        max_row = len(obstacleGrid)
        max_col = len(obstacleGrid[0])

        if obstacleGrid[max_row - 1][max_col - 1] == 1:
            return 0

        cache = [[-1] * max_col for _ in range(max_row)]
        cache[max_row - 1][max_col - 1] = 1

        def uniquePaths(row, col):
            if row >= max_row or col >= max_col:
                return 0
            if cache[row][col] != -1:
                return cache[row][col]
            if obstacleGrid[row][col] == 1:
                cache[row][col] = 0
                return 0
            res = uniquePaths(row + 1, col) + uniquePaths(row, col + 1)
            cache[row][col] = res
            return res

        return uniquePaths(0, 0)
# leetcode submit region end(Prohibit modification and deletion)
