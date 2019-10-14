#
# @lc app=leetcode.cn id=303 lang=python3
#
# [303] 区域和检索 - 数组不可变
#
# https://leetcode-cn.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (57.18%)
# Likes:    105
# Dislikes: 0
# Total Accepted:    19.4K
# Total Submissions: 33.9K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。
# 
# 示例：
# 
# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 说明:
# 
# 
# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。
# 
# 
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.A = [0]
        for i in range(len(nums)):
            self.A.append(self.A[i] + nums[i])

    def sumRange(self, i: int, j: int) -> int:
        return self.A[j + 1] - self.A[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# @lc code=end

