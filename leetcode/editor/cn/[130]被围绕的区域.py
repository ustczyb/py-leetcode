# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
# 。
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X"
# ,"X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都
# 会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["X"]]
# 输出：[["X"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 200 
#  board[i][j] 为 'X' 或 'O' 
#  
#  
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 
#  👍 497 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        visited = [[0] * n for i in range(m)]

        def dfs(row, col):
            if row < 0 or row == m:
                return
            if col < 0 or col == n:
                return
            if board[row][col] == 'X':
                return
            if visited[row][col] == 1:
                return
            visited[row][col] = 1
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for i in range(n):
            dfs(0, i)
            dfs(m - 1, i)
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)

        for i in range(len(visited)):
            for j in range(len(visited[0])):
                if visited[i][j] == 0:
                    board[i][j] = 'X'
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X" ,"X"]]
    board = [['O']]
    Solution().solve(board)
    print(board)