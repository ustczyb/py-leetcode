#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
# https://leetcode-cn.com/problems/remove-element/description/
#
# algorithms
# Easy (56.15%)
# Likes:    382
# Dislikes: 0
# Total Accepted:    90.7K
# Total Submissions: 161.6K
# Testcase Example:  '[3,2,2,3]\n3'
#
# 给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。
# 
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
# 
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
# 
# 示例 1:
# 
# 给定 nums = [3,2,2,3], val = 3,
# 
# 函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。
# 
# 你不需要考虑数组中超出新长度后面的元素。
# 
# 
# 示例 2:
# 
# 给定 nums = [0,1,2,2,3,0,4,2], val = 2,
# 
# 函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。
# 
# 注意这五个元素可为任意顺序。
# 
# 你不需要考虑数组中超出新长度后面的元素。
# 
# 
# 说明:
# 
# 为什么返回数值是整数，但输出的答案是数组呢?
# 
# 请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
# 
# 你可以想象内部操作如下:
# 
# // nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
# int len = removeElement(nums, val);
# 
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 1:
            n = nums[0]
            if n == val:
                return 0
            else:
                return 1
        end_index = len(nums) - 1
        begin_index = 0
        while(begin_index < end_index):
            begin_index = self.next_begin_index(nums=nums, val=val, begin_index=begin_index)
            end_index = self.next_end_index(nums=nums, val=val, end_index=end_index)
            if begin_index < end_index:
                self.swap(nums, begin_index, end_index)
        return end_index + 1

    def swap(self, nums: List[int], i: int, j: int):
        nums[i], nums[j] = nums[j], nums[i]
    
    def next_begin_index(self, nums: List[int], val: int, begin_index: int) -> int:
        while(begin_index < len(nums) and nums[begin_index] != val):
            begin_index += 1
        return begin_index
    
    def next_end_index(self, nums: List[int], val: int, end_index: int) -> int:
        while(end_index >= 0 and nums[end_index] == val):
            end_index -= 1
        return end_index
            
# @lc code=end

if __name__ == "__main__":
    l = [3]
    print(Solution().removeElement(l, 3))
    print(l)