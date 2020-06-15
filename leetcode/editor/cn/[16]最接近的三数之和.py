# 给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和
# 。假定每组输入只存在唯一答案。 
# 
#  
# 
#  示例： 
# 
#  输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 10^3 
#  -10^3 <= nums[i] <= 10^3 
#  -10^4 <= target <= 10^4 
#  
#  Related Topics 数组 双指针

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        min_abs_diff = abs(res - target)
        for i in range(len(nums)):
            two_res = self.twoSumClosest(nums[: i] + nums[i + 1:], target - nums[i])
            cur_res = two_res + nums[i]
            if abs(cur_res - target) < min_abs_diff:
                min_abs_diff = abs(cur_res - target)
                res = cur_res
        return res

    def twoSumClosest(self, nums: List[int], target: int) -> int:
        res = nums[0] + nums[len(nums) - 1]
        min_abs_diff = abs(res - target)
        i = 0
        j = len(nums) - 1
        while i < j:
            cur_sum = nums[i] + nums[j]
            cur_diff = cur_sum - target
            if abs(cur_diff) < min_abs_diff:
                res = cur_sum
                min_abs_diff = abs(cur_diff)
            if cur_diff > 0:
                j -= 1
            elif cur_diff < 0:
                i += 1
            else:
                return target
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
