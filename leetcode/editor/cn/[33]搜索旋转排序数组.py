# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。 
# 
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
# 
#  搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。 
# 
#  你可以假设数组中不存在重复的元素。 
# 
#  你的算法时间复杂度必须是 O(log n) 级别。 
# 
#  示例 1: 
# 
#  输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
#  
# 
#  示例 2: 
# 
#  输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1 
#  Related Topics 数组 二分查找

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.__search(nums, target, 0, len(nums) - 1)

    def __search(self, nums: List[int], target: int, begin: int, end: int) -> int:
        if begin > end:
            return -1
        mid = int((begin + end) / 2)
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[begin]:
            if target >= nums[begin] and mid > begin and target <= nums[mid - 1]:
                return self.binary_search(nums, target, begin, mid - 1)
            else:
                return self.__search(nums, target, mid + 1, end)
        else:
            if target >= nums[mid + 1] and target <= nums[end]:
                return self.binary_search(nums, target, mid + 1, end)
            else:
                return self.__search(nums, target, begin, mid - 1)

    def binary_search(self, nums: List[int], target: int, begin: int, end: int) -> int:
        if begin > end:
            return -1
        mid = int((begin + end) / 2)
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.binary_search(nums, target, begin, mid - 1)
        else:
            return self.binary_search(nums, target, mid + 1, end)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().search([3, 4, 5, 6, 7, 8, 1, 2], 2))
