# 给定一个非负整数数组，你最初位于数组的第一个位置。 
# 
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。 
# 
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。 
# 
#  示例: 
# 
#  输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#  
# 
#  说明: 
# 
#  假设你总是可以到达数组的最后一个位置。 
#  Related Topics 贪心算法 数组 
#  👍 937 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def jump(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 0

        n = len(nums)
        cache = [-1] * n
        cache[n - 1] = 0

        def min_steps(i):
            if nums[i] == 0:
                return n
            if cache[i] != -1:
                return cache[i]
            if i + nums[i] >= n - 1:
                cache[i] = 1
                return cache[i]
            res = 1 + min([min_steps(i + j + 1) for j in range(nums[i])])
            cache[i] = res
            return cache[i]

        return min_steps(0)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().jump([2, 3, 0, 1, 4]))
