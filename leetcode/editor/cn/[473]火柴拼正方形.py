# 还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。不能折断火柴，可以把火柴连接起来，并且每根火柴
# 都要用到。 
# 
#  输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。 
# 
#  示例 1: 
# 
#  
# 输入: [1,1,2,2,2]
# 输出: true
# 
# 解释: 能拼成一个边长为2的正方形，每边两根火柴。
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,3,3,3,4]
# 输出: false
# 
# 解释: 不能用所有火柴拼成一个正方形。
#  
# 
#  注意: 
# 
#  
#  给定的火柴长度和在 0 到 10^9之间。 
#  火柴数组的长度不超过15。 
#  
#  Related Topics 位运算 数组 动态规划 回溯 状态压缩 
#  👍 193 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        circle = sum(matchsticks)
        if circle % 4 != 0:
            return False
        matchsticks = sorted(matchsticks, reverse=True)

        def backtrack(nums: List[int], index: int, target: int, size: List[int]) -> bool:
            if index == len(nums):
                if size[0] == size[1] == size[2] == size[3]:
                    return True
                return False
            else:
                for i in range(len(size)):
                    if size[i] + nums[index] > target:
                        continue
                    size[i] += nums[index]
                    if backtrack(nums, index + 1, target, size):
                        return True
                    size[i] -= nums[index]
            return False

        sizes = [0] * 4
        return backtrack(matchsticks, 0, int(circle / 4), sizes)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [3, 3, 3, 3, 4]
    print(Solution().makesquare(nums))
