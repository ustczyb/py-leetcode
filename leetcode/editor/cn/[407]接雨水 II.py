# 给你一个 m x n 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
# 输出: 4
# 解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
# 输出: 10
#  
# 
#  
# 
#  提示: 
# 
#  
#  m == heightMap.length 
#  n == heightMap[i].length 
#  1 <= m, n <= 200 
#  0 <= heightMap[i][j] <= 2 * 104 
#  
# 
#  
#  Related Topics 广度优先搜索 数组 矩阵 堆（优先队列） 
#  👍 372 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
import sys
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        rows = len(heightMap)
        cols = len(heightMap[0])

        # 1.初始化图
        visited_map = [[-1] * cols for _ in range(rows)]

        # 2.图扩散
        def check(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return False
            return True

        def is_zero_component(row, col):
            if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
                return True
            # if heightMap[row][col] >= heightMap[row][0] or heightMap[row][col] >= heightMap[row][cols - 1] or heightMap[row][col] >= heightMap[0][col] or heightMap[row][col] >= heightMap[rows - 1][col]:
            #     return True
            return False

        for i in range(rows):
            for j in range(cols):
                if is_zero_component(i, j):
                    visited_map[i][j] = 0

        # def dfs(row, col):
        #     if visited_map[row][col] != -1:
        #         return
        #     visited_map[row][col] = 0
        #     next = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        #     for d_r, d_c in next:
        #         if check(row + d_r, col + d_c) and (row + d_r == 0 or row + d_r == rows - 1 or col + d_c == 0 or col + d_c == -1 or heightMap[row][col] <= heightMap[row + d_r][col + d_c]):
        #             dfs(row + d_r, col + d_c)

        # 3.对每个联通分量
        id_height_map = {}
        id = 0

        def dfs2(row, col):
            if visited_map[row][col] != -1:
                return
            visited_map[row][col] = id
            next = [(-1, 0), (1, 0), (0, 1), (0, -1)]
            for d_r, d_c in next:
                if visited_map[row + d_r][col + d_c] == 0:
                    if id_height_map[id] > heightMap[row + d_r][col + d_c]:
                        id_height_map[id] = heightMap[row + d_r][col + d_c]
                else:
                    dfs2(row + d_r, col + d_c)

        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if visited_map[row][col] == -1:
                    id += 1
                    id_height_map[id] = sys.maxsize
                    dfs2(row, col)
        res = 0
        for row in range(1, rows - 1):
            for col in range(1, cols - 1):
                if visited_map[row][col] > 0:
                    res += id_height_map[visited_map[row][col]] - heightMap[row][col]
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
    # heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
    heightMap = [[14, 17, 18, 16, 14, 16],
                 [17, 3,  10, 2,  3,  8],
                 [11, 10, 4,  7,  1,  7],
                 [13, 7,  2,  9,  8,  10],
                 [13, 1,  3,  4,  8,  6],
                 [20, 3,  3,  9,  10, 8]]
    print(Solution().trapRainWater(heightMap))
