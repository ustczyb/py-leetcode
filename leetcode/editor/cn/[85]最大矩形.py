# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。 
# 
#  示例: 
# 
#  输入:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# 输出: 6 
#  Related Topics 栈 数组 哈希表 动态规划

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        max_size = 0
        cur_arr = [int(x) for x in matrix[0]]
        for row in range(len(matrix)):
            if row > 0:
                for i in range(len(matrix[0])):
                    cur_arr[i] = cur_arr[i] + int(matrix[row][i]) if matrix[row][i] == '1' else 0
            cur_max_rec = self.maxRectangle(cur_arr)
            if cur_max_rec > max_size:
                max_size = cur_max_rec
        return max_size

    def maxRectangle(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i in range(len(heights)):
            if not stack or heights[stack[-1]] < heights[i]:
                stack.append(i)
            else:
                while stack and heights[stack[-1]] > heights[i]:
                    top = stack.pop()
                    if stack:
                        cur_area = heights[top] * (i - stack[-1] - 1)
                    else:
                        cur_area = heights[top] * i
                    if cur_area > max_area:
                        max_area = cur_area
                stack.append(i)
        while stack:
            top = stack.pop()
            if stack:
                cur_area = heights[top] * (len(heights) - stack[-1] - 1)
            else:
                cur_area = heights[top] * (len(heights))
            if cur_area > max_area:
                max_area = cur_area
        return max_area


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    # matrix = [
    #     ["1", "0", "1", "0", "0"],
    #     ["1", "0", "1", "1", "1"],
    #     ["1", "1", "1", "1", "1"],
    #     ["1", "0", "0", "1", "0"]
    # ]
    matrix = [["0","1"],["1","0"]]
    print(Solution().maximalRectangle(matrix))
    # print(Solution().maxRectangle([2, 1, 5, 6, 2, 3]))
