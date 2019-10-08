#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
# https://leetcode-cn.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (35.93%)
# Likes:    111
# Dislikes: 0
# Total Accepted:    22.5K
# Total Submissions: 62.5K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j
# 的差的绝对值最大为 k。
# 
# 示例 1:
# 
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
# 
# 示例 2:
# 
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
# 
# 示例 3:
# 
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
# 
#
from typing import List
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        if k <= 0 or l == 1:
            return False
        if k >= l:
            return l != len(set(nums))
        s = set(nums[:k+1])
        # 前k个元素有重复元素
        if len(s) < k+1:
            return True
        else:
            for i in range(0, l - k - 1):
                s.remove(nums[i])
                if nums[i + k + 1] in s:
                    return True
                else:
                    s.add(nums[i + k + 1])
        return False
        

# @lc code=end
if __name__ == "__main__":
    print(Solution().containsNearbyDuplicate([1, 1], 2))