# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
# 
#  你的算法时间复杂度必须是 O(log n) 级别。 
# 
#  如果数组中不存在目标值，返回 [-1, -1]。 
# 
#  示例 1: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4] 
# 
#  示例 2: 
# 
#  输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1] 
#  Related Topics 数组 二分查找

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def search(self, nums: List[int], target: int, begin: int, end: int, order: int):
        if begin > end:
            return -1
        if begin == end:
            if nums[begin] == target:
                return begin
            else:
                return -1
        mid = int((begin + end) / 2)
        if nums[mid] > target:
            return self.search(nums, target, begin, mid - 1, order)
        if nums[mid] < target:
            return self.search(nums, target, mid + 1, end, order)
        else:
            if order == 0:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    return self.search(nums, target, begin, mid - 1, order)
            else:
                if nums[mid + 1] > target:
                    return mid
                else:
                    return self.search(nums, target, mid + 1, end, order)

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.search(nums, target, 0, len(nums) - 1, 0),
                self.search(nums, target, 0, len(nums) - 1, 1)]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 5))
