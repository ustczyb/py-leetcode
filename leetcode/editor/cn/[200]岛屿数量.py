# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1: 
# 
#  输入:
# [
# ['1','1','1','1','0'],
# ['1','1','0','1','0'],
# ['1','1','0','0','0'],
# ['0','0','0','0','0']
# ]
# 输出: 1
#  
# 
#  示例 2: 
# 
#  输入:
# [
# ['1','1','0','0','0'],
# ['1','1','0','0','0'],
# ['0','0','1','0','0'],
# ['0','0','0','1','1']
# ]
# 输出: 3
# 解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def getF(self, arr, i):
        if arr[i] == i:
            return i
        else:
            arr[i] = self.getF(arr, arr[i])
            return arr[i]

    def union(self, arr, i, j):
        root_i = self.getF(arr, i)
        root_j = self.getF(arr, j)
        if root_i < root_j:
            arr[root_j] = root_i
        if root_j < root_i:
            arr[root_i] = root_j

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        arr = [-1] * (m * n)
        island_dict = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                arr[i * n + j] = i * n + j
                if i > 0 and grid[i - 1][j] == '1':
                    self.union(arr, i * n + j, (i - 1) * n + j)
                if j > 0 and grid[i][j - 1] == '1':
                    self.union(arr, i * n + j, i * n + j - 1)
        iland_set = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                iland_set.add(self.getF(arr, i * n + j))
        return len(iland_set)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    grid = [['1', '1', '1'],
            ['0', '1', '0'],
            ['1', '1', '1']]
    print(Solution().numIslands(grid))
