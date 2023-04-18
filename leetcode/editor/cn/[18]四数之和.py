#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode-cn.com/problems/4sum/description/
#
# algorithms
# Medium (35.93%)
# Likes:    360
# Dislikes: 0
# Total Accepted:    49.7K
# Total Submissions: 135.8K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c
# + d 的值与 target 相等？找出所有满足条件且不重复的四元组。
# 
# 注意：
# 
# 答案中不可以包含重复的四元组。
# 
# 示例：
# 
# 给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#
from typing import List
# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            nums.sort()
            res = []
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                sub_res = self.threeSum(nums[i + 1:], target - nums[i])
                if sub_res:
                    for sub_list in sub_res:
                        sub_list.insert(0, nums[i])
                    res.extend(sub_res)
            return res


    def threeSum(self, sorted_nums: List[int], target: int) -> List[List[int]]:
        if len(sorted_nums) < 3:
            return []
        res = []
        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            sub_res = self.twoSum(sorted_nums[i + 1:], target - sorted_nums[i])
            if sub_res:
                for sub_list in sub_res:
                    sub_list.insert(0, sorted_nums[i])
                res.extend(sub_res)
        return res


    def twoSum(self, sorted_nums: List[int], target: int) -> List[List[int]]:
        if len(sorted_nums) < 2:
            return []
        if sorted_nums[0] + sorted_nums[1] > target:
            return []
        begin_index = 0
        end_index = len(sorted_nums) - 1
        res = []
        while begin_index < end_index:
            if sorted_nums[begin_index] + sorted_nums[end_index] == target:
                res.append([sorted_nums[begin_index], sorted_nums[end_index]])
                while begin_index < len(sorted_nums) - 1 and sorted_nums[begin_index + 1] == sorted_nums[begin_index]:
                    begin_index += 1
                begin_index += 1
                while end_index > 0 and sorted_nums[end_index - 1] == sorted_nums[end_index]:
                    end_index -= 1
                end_index -= 1
            elif sorted_nums[begin_index] + sorted_nums[end_index] < target:
                begin_index += 1
            else:
                end_index -= 1
        return res
# @lc code=end

if __name__ == "__main__":
    l = [-1, 0, -5, -2, -2, -4, 0, 1, -2]
    res = Solution().fourSum(l, -9)
    print(res)