# 给你一个未排序的整数数组，请你找出其中没有出现的最小的正整数。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [1,2,0]
# 输出: 3
#  
# 
#  示例 2: 
# 
#  输入: [3,4,-1,1]
# 输出: 2
#  
# 
#  示例 3: 
# 
#  输入: [7,8,9,11,12]
# 输出: 1
#  
# 
#  
# 
#  提示： 
# 
#  你的算法的时间复杂度应为O(n)，并且只能使用常数级别的额外空间。 
#  Related Topics 数组

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def swap(self, nums: List[int], i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            while 1 <= nums[i] <= size and nums[i] != nums[nums[i] - 1]:
                self.swap(nums, i, nums[i] - 1)

        for i in range(size):
            if i + 1 != nums[i]:
                return i + 1

        return size + 1


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().firstMissingPositive([3, 4, -1, 1]))
