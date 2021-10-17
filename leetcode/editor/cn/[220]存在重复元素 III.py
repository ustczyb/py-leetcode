# 给你一个整数数组 nums 和两个整数 k 和 t 。请你判断是否存在 两个不同下标 i 和 j，使得 abs(nums[i] - nums[j]) <= 
# t ，同时又满足 abs(i - j) <= k 。 
# 
#  如果存在则返回 true，不存在返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3,1], k = 3, t = 0
# 输出：true 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,0,1,1], k = 1, t = 2
# 输出：true 
# 
#  示例 3： 
# 
#  
# 输入：nums = [1,5,9,1,5,9], k = 2, t = 3
# 输出：false 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 2 * 104 
#  -231 <= nums[i] <= 231 - 1 
#  0 <= k <= 104 
#  0 <= t <= 231 - 1 
#  
#  Related Topics 数组 桶排序 有序集合 排序 滑动窗口 
#  👍 495 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
# 思路： k+1的滑动窗口 计算滑动窗口中排序后相邻两数之差是否<t即可
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
# leetcode submit region end(Prohibit modification and deletion)
