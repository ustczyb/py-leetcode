# 给定一个三角形 triangle ，找出自顶向下的最小路径和。 
# 
#  每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果
# 正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#  
# 
#  示例 2： 
# 
#  
# 输入：triangle = [[-10]]
# 输出：-10
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= triangle.length <= 200 
#  triangle[0].length == 1 
#  triangle[i].length == triangle[i - 1].length + 1 
#  -104 <= triangle[i][j] <= 104 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？ 
#  
#  Related Topics 数组 动态规划 
#  👍 743 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        max_row = len(triangle)
        arr1 = triangle[-1]
        arr2 = [-1] * max_row

        for i in range(max_row - 1, 0, -1):
            if (max_row - i) % 2 == 1:
                # arr1 -> arr2
                for j in range(i):
                    arr2[j] = triangle[i - 1][j] + min(arr1[j], arr1[j + 1])
            else:
                # arr2 -> arr1
                for j in range(i):
                    arr1[j] = triangle[i - 1][j] + min(arr2[j], arr2[j + 1])
        if max_row % 2 == 0:
            return arr2[0]
        else:
            return arr1[0]

        # max_row = len(triangle)
        # cache = [[-1] * (i + 1) for i in range(len(triangle))]
        #
        # def min_path(row, col):
        #     if row == max_row or col > row:
        #         return 0
        #     if cache[row][col] != -1:
        #         return cache[row][col]
        #     res = triangle[row][col] + min(min_path(row + 1, col), min_path(row + 1, col + 1))
        #     cache[row][col] = res
        #     return res
        # return min_path(0, 0)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    print(Solution().minimumTotal(triangle))