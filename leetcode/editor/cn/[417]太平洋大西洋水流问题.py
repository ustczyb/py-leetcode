# 给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。 
# 
#  规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。 
# 
#  请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。 
# 
#  
# 
#  提示： 
# 
#  
#  输出坐标的顺序不重要 
#  m 和 n 都小于150 
#  
# 
#  
# 
#  示例： 
# 
#  
# 
#  
# 给定下面的 5x5 矩阵:
# 
#   太平洋 ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * 大西洋
# 
# 返回:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
#  
# 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 
#  👍 268 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        reach_left_up = [[-1] * cols for _ in range(rows)]
        reach_right_down = [[-1] * cols for _ in range(rows)]
        for i in range(rows):
            reach_left_up[i][0] = 1
            reach_right_down[i][cols - 1] = 1
        for i in range(cols):
            reach_left_up[0][i] = 1
            reach_right_down[rows - 1][i] = 1

        left_up_queue = [(i, 0) for i in range(rows)] + [(0, i) for i in range(cols)]
        right_down_queue = [(i, cols - 1) for i in range(rows)] + [(rows - 1, i) for i in range(cols)]

        next_step = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isOverboard(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return True
            return False

        while left_up_queue:
            row, col = left_up_queue.pop()
            if reach_left_up[row][col] != -1:
                for d_r, d_c in next_step:
                    if not isOverboard(row + d_r, col + d_c) and reach_left_up[row + d_r][col + d_c] == -1:
                        if heights[row + d_r][col + d_c] >= heights[row][col]:
                            reach_left_up[row + d_r][col + d_c] = 1
                            left_up_queue.insert(0, (row + d_r, col + d_c))

        while right_down_queue:
            row, col = right_down_queue.pop()
            if reach_right_down[row][col] != -1:
                for d_r, d_c in next_step:
                    if not isOverboard(row + d_r, col + d_c) and reach_right_down[row + d_r][col + d_c] == -1:
                        if heights[row + d_r][col + d_c] >= heights[row][col]:
                            reach_right_down[row + d_r][col + d_c] = 1
                            right_down_queue.insert(0, (row + d_r, col + d_c))
        res = []
        for r in range(rows):
            for c in range(cols):
                if reach_left_up[r][c] == 1 and reach_right_down[r][c] == 1:
                    res.append([r, c])
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    ocean = [[1, 2, 2, 3, 5],
             [3, 2, 3, 4, 4],
             [2, 4, 5, 3, 1],
             [6, 7, 1, 4, 5],
             [5, 1, 1, 2, 4]]
    print(Solution().pacificAtlantic(ocean))
