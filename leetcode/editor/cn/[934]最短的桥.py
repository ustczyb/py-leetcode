# 在给定的二维二进制数组 A 中，存在两座岛。（岛是由四面相连的 1 形成的一个最大组。） 
# 
#  现在，我们可以将 0 变为 1，以使两座岛连接起来，变成一座岛。 
# 
#  返回必须翻转的 0 的最小数目。（可以保证答案至少是 1 。） 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：A = [[0,1],[1,0]]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：A = [[0,1,0],[0,0,0],[0,0,1]]
# 输出：2
#  
# 
#  示例 3： 
# 
#  
# 输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# 输出：1 
# 
#  
# 
#  提示： 
# 
#  
#  2 <= A.length == A[0].length <= 100 
#  A[i][j] == 0 或 A[i][j] == 1 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 
#  👍 173 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        # 1.bfs找到两座岛
        visited = [[0] * len(grid[0]) for _ in range(len(grid))]
        queue = []
        rows = len(grid)
        cols = len(grid[0])
        no = 1

        next_steps = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_overboard(row, col):
            return row < 0 or col < 0 or row >= rows or col >= cols

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and not visited[row][col]:
                    visited[row][col] = no
                    queue.insert(0, (row, col))
                    while queue:
                        row, col = queue.pop()
                        for d_r, d_c in next_steps:
                            next_row = row + d_r
                            next_col = col + d_c
                            if not is_overboard(next_row, next_col) and grid[next_row][next_col] == 1 and not visited[next_row][next_col]:
                                visited[next_row][next_col] = no
                                queue.insert(0, (next_row, next_col))
                    no += 1
        # 2.bfs找到最短路径
        dist = [[-1] * len(grid[0]) for _ in range(len(grid))]
        queue = []
        for row in range(rows):
            for col in range(cols):
                if visited[row][col] == 1:
                    dist[row][col] = 0
                    queue.insert(0, (row, col))
        while queue:
            row, col = queue.pop()
            for d_r, d_c in next_steps:
                next_row = row + d_r
                next_col = col + d_c
                if not is_overboard(next_row, next_col) and dist[next_row][next_col] == -1:
                    if visited[next_row][next_col] == 2:
                        return dist[row][col]
                    dist[next_row][next_col] = dist[row][col] + 1
                    queue.insert(0, (next_row, next_col))

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
    print(Solution().shortestBridge(A))