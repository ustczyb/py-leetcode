# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Mar
# cos 贡献此图。 
# 
#  示例: 
# 
#  输入: [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出: 6
# O(n) O(1)解
#  Related Topics 栈 数组 双指针

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        left_stack = [0]
        right_stack = [0]
        n = len(height)
        for i in range(1, n):
            left_stack.append(max(left_stack[-1], height[i - 1]))
            right_stack.append(max(right_stack[-1], height[n - i]))
        res = 0
        for i in range(n):
            res += max((min(left_stack[i], right_stack[n - 1 - i]) - height[i]), 0)
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    heights = [2, 0, 2]
    print(Solution().trap(heights))
