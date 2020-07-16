# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。 
# 
#  求在该柱状图中，能够勾勒出来的矩形的最大面积。 
# 
#  
# 
#  
# 
#  以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。 
# 
#  
# 
#  
# 
#  图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。 
# 
#  
# 
#  示例: 
# 
#  输入: [2,1,5,6,2,3]
# 输出: 10 
#  Related Topics 栈 数组

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
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
    print(Solution().largestRectangleArea([2,1,5,6,2,3]))
