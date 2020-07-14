# 给定一个范围在 1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。 
# 
#  找到所有在 [1, n] 范围之间没有出现在数组中的数字。 
# 
#  您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。 
# 
#  示例: 
# 
#  
# 输入:
# [4,3,2,7,8,2,3,1]
# 
# 输出:
# [5,6]
#  
#  Related Topics 数组

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        index = 0
        while index < len(nums):
            while nums[index] != index + 1 and nums[nums[index] - 1] != nums[index]:
                self.swap(nums, index, nums[index] - 1)
            index += 1
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res

    def swap(self, nums: List[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    l = [4,3,2,7,8,2,3,1]
    print(Solution().findDisappearedNumbers(l))
