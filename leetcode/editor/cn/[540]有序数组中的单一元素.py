# 给定一个只包含整数的有序数组，每个元素都会出现两次，唯有一个数只会出现一次，找出这个数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [1,1,2,3,3,4,4,8,8]
# 输出: 2
#  
# 
#  示例 2: 
# 
#  
# 输入: nums =  [3,3,7,7,10,11,11]
# 输出: 10
#  
# 
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= nums.length <= 105 
#  0 <= nums[i] <= 105 
#  
# 
#  
# 
#  进阶: 采用的方案可以在 O(log n) 时间复杂度和 O(1) 空间复杂度中运行吗？ 
#  Related Topics 数组 二分查找 
#  👍 250 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        high = len(nums) - 1
        low = 0
        mid = int((high + low) / 2)
        if nums[mid - 1] == nums[mid]:
            if mid % 2 == 1:
                return self.singleNonDuplicate(nums[mid + 1:])
            else:
                return self.singleNonDuplicate(nums[:mid - 1])
        elif nums[mid + 1] == nums[mid]:
            if mid % 2 == 1:
                return self.singleNonDuplicate(nums[:mid])
            else:
                return self.singleNonDuplicate(nums[mid + 2:])
        else:
            return nums[mid]
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [3,3,7,7,10,11,11]
    print(Solution().singleNonDuplicate(nums))