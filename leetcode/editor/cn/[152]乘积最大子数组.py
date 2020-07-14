# 给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
#  
# 
#  示例 2: 
# 
#  输入: [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。 
#  Related Topics 数组 动态规划

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i]表示以第i个元素结尾的乘积最大的连续子数组
        pos_dp = [0] * len(nums)
        neg_dp = [0] * len(nums)
        pos_dp[0] = nums[0]
        neg_dp[0] = nums[0]
        for i in range(1, len(nums)):
            pos_dp[i] = max(pos_dp[i - 1] * nums[i], neg_dp[i - 1] * nums[i], nums[i])
            neg_dp[i] = min(pos_dp[i - 1] * nums[i], neg_dp[i - 1] * nums[i], nums[i])
        return max(pos_dp)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().maxProduct([2, -5, -2, -4, 3]))
    # print([[0]] * 3)
