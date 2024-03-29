# 给定一个含有 n 个正整数的数组和一个正整数 target 。 
# 
#  找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长
# 度。如果不存在符合条件的子数组，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
#  
# 
#  示例 2： 
# 
#  
# 输入：target = 4, nums = [1,4,4]
# 输出：1
#  
# 
#  示例 3： 
# 
#  
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= target <= 109 
#  1 <= nums.length <= 105 
#  1 <= nums[i] <= 105 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。 
#  
#  Related Topics 数组 二分查找 前缀和 滑动窗口 
#  👍 753 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_index = 0
        right_index = 0
        if not nums:
            return 0
        cur_sum = nums[0]
        res = len(nums) + 1
        while right_index < len(nums):
            if cur_sum >= target:
                if res > right_index - left_index + 1:
                    res = right_index - left_index + 1
                cur_sum -= nums[left_index]
                left_index += 1
            else:
                right_index += 1
                if right_index >= len(nums):
                    break
                cur_sum += nums[right_index]
        if res == len(nums) + 1:
            return 0
        return res
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    target = 4
    nums = [1, 4, 4]
    print(Solution().minSubArrayLen(target, nums))