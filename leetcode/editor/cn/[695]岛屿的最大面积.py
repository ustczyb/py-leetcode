# 给定一个包含了一些 0 和 1 的非空二维数组 grid 。 
# 
#  一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 
# 0（代表水）包围着。 
# 
#  找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。) 
# 
#  
# 
#  示例 1: 
# 
#  [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
#  
# 
#  对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。 
# 
#  示例 2: 
# 
#  [[0,0,0,0,0,0,0,0]] 
# 
#  对于上面这个给定的矩阵, 返回 0。 
# 
#  
# 
#  注意: 给定的矩阵grid 的长度和宽度都不超过 50。 
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 
#  👍 516 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        row_nums = len(grid)
        col_nums = len(grid[0])

        root_dict = {}

        def get_index(row, col):
            return row * col_nums + col

        def union(p, q):
            root_p = find(p)
            root_q = find(q)
            if root_p != root_q:
                root_dict[root_p] = root_dict[root_q]

        def find(p):
            if p != root_dict[p]:
                root_dict[p] = find(root_dict[p])
            return root_dict[p]

        for row in range(row_nums):
            for col in range(col_nums):
                if grid[row][col]:
                    index = get_index(row, col)
                    root_dict[index] = index
                    if row > 0 and grid[row - 1][col]:
                        union(index, get_index(row - 1, col))
                    if col > 0 and grid[row][col - 1]:
                        union(index, get_index(row, col - 1))

        counter = defaultdict(int)
        for i in root_dict:
            counter[find(i)] += 1
        res = 0
        for k in counter:
            if counter[k] > res:
                res = counter[k]
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    # grid = [[0,0,0,0,0,0,0,0]]
    print(Solution().maxAreaOfIsland(grid))
