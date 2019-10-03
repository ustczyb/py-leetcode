#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (44.32%)
# Likes:    326
# Dislikes: 0
# Total Accepted:    77.4K
# Total Submissions: 174.7K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, 0, len(nums) - 1, target)
    def binarySearch(self, nums: List[int], begin_index: int, end_index: int, target: int) -> int:
        if begin_index >= end_index:
            if target > nums[begin_index]:
                return begin_index + 1
            else:
                return begin_index
        mid = int((begin_index + end_index) / 2)
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.binarySearch(nums, begin_index, mid - 1, target)
        if nums[mid] < target:
            return self.binarySearch(nums, mid + 1, end_index, target)
        
# @lc code=end

if __name__ == "__main__":
    l = [1, 3]
    target = 0
    print(Solution().searchInsert(l, target))