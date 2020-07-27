# 给定一个未排序的整数数组，找出最长连续序列的长度。 
# 
#  要求算法的时间复杂度为 O(n)。 
# 
#  示例: 
# 
#  输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。 
#  Related Topics 并查集 数组

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        dp = [0] * len(nums)    # 以nums[i]结尾的连续序列长度
        def find(i):
            num = nums[i]
            if not dp[i]:
                if num - 1 not in d:
                    dp[i] = 1
                else:
                    dp[i] = 1 + find(d[num - 1])
            return dp[i]
        for i in range(len(nums)):
            find(i)
        return max(dp)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
