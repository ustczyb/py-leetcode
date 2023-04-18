# 给你一个下标从 0 开始的 m x n 整数矩阵 grid 。你一开始的位置在 左上角 格子 (0, 0) 。 
# 
#  当你在格子 (i, j) 的时候，你可以移动到以下格子之一： 
# 
#  
#  满足 j < k <= grid[i][j] + j 的格子 (i, k) （向右移动），或者 
#  满足 i < k <= grid[i][j] + i 的格子 (k, j) （向下移动）。 
#  
# 
#  请你返回到达 右下角 格子 (m - 1, n - 1) 需要经过的最少移动格子数，如果无法到达右下角格子，请你返回 -1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  输入：grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
# 输出：4
# 解释：上图展示了到达右下角格子经过的 4 个格子。
#  
# 
#  示例 2： 
# 
#  
# 
#  输入：grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
# 输出：3
# 解释：上图展示了到达右下角格子经过的 3 个格子。
#  
# 
#  示例 3： 
# 
#  
# 
#  输入：grid = [[2,1,0],[1,0,0]]
# 输出：-1
# 解释：无法到达右下角格子。
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 10⁵ 
#  1 <= m * n <= 10⁵ 
#  0 <= grid[i][j] < m * n 
#  grid[m - 1][n - 1] == 0 
#  
# 
#  Related Topics 栈 并查集 树状数组 线段树 数组 二分查找 动态规划 👍 12 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        cache = [[-2] * len(grid[0]) for _ in range(len(grid))]
        cache[len(grid) - 1][len(grid[0]) - 1] = 1

        union_find_row = [list(range(len(grid[0]) + 1)) for _ in range(len(grid))]
        union_find_col = [list(range(len(grid) + 1)) for _ in range(len(grid[0]))]
        # union_find_row[len(grid) - 1][len(grid[0]) - 1] = len(grid[0])
        # union_find_col[len(grid[0]) - 1][len(grid) - 1] = len(grid)

        def find_next(is_row, row_index, col_index):
            uf = union_find_row[row_index] if is_row else union_find_col[row_index]
            if col_index != uf[col_index]:
                uf[col_index] = find_next(is_row, row_index, uf[col_index])
            return uf[col_index]

        def min_visit_cell(row, col):
            print(row, col)
            if cache[row][col] != -2:
                return cache[row][col]
            if row >= len(grid) or col >= len(grid[0]):
                return -1
            res = len(grid[0]) + len(grid) + 1
            # search row
            k = col + 1
            while k < min(grid[row][col] + col + 1, len(grid[0])):
                sub_res = min_visit_cell(row, k)
                # union_find_row[row][col] = col + 1
                if sub_res != -1:
                    res = min(res, sub_res)
                l = find_next(True, row, k)
                if l == k: #and l == len(grid[0]) - 1:
                    break
                k = l
            # search col
            k = row + 1
            while k < min(grid[row][col] + row + 1, len(grid)):
                sub_res = min_visit_cell(k, col)
                # union_find_col[col][row] = row + 1
                if sub_res != -1:
                    res = min(res, sub_res)
                l = find_next(False, col, k)
                if l == k: #and l == len(grid) - 1:
                    break
                k = l
            if res == len(grid[0]) + len(grid) + 1:
                cache[row][col] = -1
                # 搜索后发现失败 后面跳过这个位置
                union_find_row[row][col] = col + 1
                union_find_col[col][row] = row + 1
            else:
                cache[row][col] = res + 1
            return cache[row][col]

        return min_visit_cell(0, 0)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # grid = [[2],[1],[3],[0]]
    grid = [[3, 4, 2, 1], [4, 2, 3, 1], [2, 1, 0, 0], [2, 4, 0, 0]]
    print(Solution().minimumVisitedCells(grid))