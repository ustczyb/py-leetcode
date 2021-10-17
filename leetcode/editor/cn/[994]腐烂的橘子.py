# 在给定的网格中，每个单元格可以有以下三个值之一： 
# 
#  
#  值 0 代表空单元格； 
#  值 1 代表新鲜橘子； 
#  值 2 代表腐烂的橘子。 
#  
# 
#  每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。 
# 
#  返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：[[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
#  
# 
#  示例 2： 
# 
#  输入：[[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
#  
# 
#  示例 3： 
# 
#  输入：[[0,2]]
# 输出：0
# 解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= grid.length <= 10 
#  1 <= grid[0].length <= 10 
#  grid[i][j] 仅为 0、1 或 2 
#  
#  Related Topics 广度优先搜索 数组 矩阵 
#  👍 423 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        normal_nums = 0
        rot_queue = []
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        max_minutes = 0
        rows = len(grid)
        cols = len(grid[0])
        next_step = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def is_overboard(row, col):
            if row >= 0 and row < rows and col >= 0 and col < cols:
                return False
            return True


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    normal_nums += 1
                if grid[row][col] == 2:
                    rot_queue.append((row, col, 0))
        while rot_queue:
            row, col, minutes = rot_queue.pop(0)
            if visited[row][col] == 0:
                if minutes > max_minutes:
                    max_minutes = minutes
                visited[row][col] = 1
                if grid[row][col] == 1:
                    grid[row][col] = 2
                    normal_nums -= 1
                for d_r, d_c in next_step:
                    next_row = row + d_r
                    next_col = col + d_c
                    if not is_overboard(next_row, next_col) and visited[next_row][next_col] == 0 and grid[next_row][next_col] == 1:
                        rot_queue.append((next_row, next_col, minutes + 1))

        return max_minutes if normal_nums == 0 else -1

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    grid = [[2,2],[1,1],[0,0],[2,0]]
    print(Solution().orangesRotting(grid))