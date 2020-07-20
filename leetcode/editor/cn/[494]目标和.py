# 给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选
# 择一个符号添加在前面。 
# 
#  返回可以使最终数组和为目标数 S 的所有添加符号的方法数。 
# 
#  
# 
#  示例： 
# 
#  输入：nums: [1, 1, 1, 1, 1], S: 3
# 输出：5
# 解释：
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# 一共有5种方法让最终目标和为3。
#  
# 
#  
# 
#  提示： 
# 
#  
#  数组非空，且长度不会超过 20 。 
#  初始的数组的和不会超过 1000 。 
#  保证返回的最终结果能被 32 位整数存下。 
#  
#  Related Topics 深度优先搜索 动态规划

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        dp_dict = {}
        size = len(nums)

        # 求的值是dp[0, S]  dp[i, n] = dp[i + 1, n - nums[i]] + dp[i + 1, n + nums[i]]
        def findSubSolution(begin_index: int, target: int) -> int:
            if begin_index == size:
                return 0 if target != 0 else 1
            key = '%d_%d' % (begin_index, target)
            if key in dp_dict:
                return dp_dict[key]
            res = findSubSolution(begin_index + 1, target + nums[begin_index]) + findSubSolution(begin_index + 1,
                                                                                                 target - nums[
                                                                                                     begin_index])
            dp_dict[key] = res
            return res

        return findSubSolution(0, S)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
