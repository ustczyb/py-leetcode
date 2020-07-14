# 实现获取下一个排列的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。 
# 
#  如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。 
# 
#  必须原地修改，只允许使用额外常数空间。 
# 
#  以下是一些例子，输入位于左侧列，其相应输出位于右侧列。 
# 1,2,3 → 1,3,2 
# 3,2,1 → 1,2,3 
# 1,1,5 → 1,5,1 
#  Related Topics 数组

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        if i == -1:
            nums.reverse()
            return

        j = i + 1
        while j < len(nums):
            if nums[j] > nums[i] and ((j == len(nums) - 1) or (nums[j + 1] <= nums[i])):
                break
            j += 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = list(reversed(nums[i + 1:]))


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    l = [1, 5, 1]
    Solution().nextPermutation(l)
    print(l)
