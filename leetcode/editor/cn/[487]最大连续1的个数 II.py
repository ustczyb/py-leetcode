# 给定一个二进制数组，你可以最多将 1 个 0 翻转为 1，找出其中最大连续 1 的个数。 
# 
#  示例 1： 
# 
#  输入：[1,0,1,1,0]
# 输出：4
# 解释：翻转第一个 0 可以得到最长的连续 1。
#      当翻转以后，最大连续 1 的个数为 4。
#  
# 
#  
# 
#  注： 
# 
#  
#  输入数组只包含 0 和 1. 
#  输入数组的长度为正整数，且不超过 10,000 
#  
# 
#  
# 
#  进阶： 
# 如果输入的数字是作为 无限流 逐个输入如何处理？换句话说，内存不能存储下所有从流中输入的数字。您可以有效地解决吗？ 
#  Related Topics 数组 动态规划 滑动窗口 
#  👍 72 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_res = 0
        max_with_flip = 0
        max_without_flip = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                max_without_flip += 1
                max_with_flip += 1
            else:
                max_with_flip = max_without_flip + 1
                max_without_flip = 0
            if max_with_flip > max_res:
                max_res = max_with_flip
        return max_res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [1, 0, 1, 1, 0]
    print(Solution().findMaxConsecutiveOnes(nums))
