# 给定两个大小为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。 
# 
#  请你找出这两个正序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。 
# 
#  你可以假设 nums1 和 nums2 不会同时为空。 
# 
#  
# 
#  示例 1: 
# 
#  nums1 = [1, 3]
# nums2 = [2]
# 
# 则中位数是 2.0
#  
# 
#  示例 2: 
# 
#  nums1 = [1, 2]
# nums2 = [3, 4]
# 
# 则中位数是 (2 + 3)/2 = 2.5
#  
#  Related Topics 数组 二分查找 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:

    def findMedian(self, nums: List[int]):
        l = len(nums)
        return (nums[int((l - 1) / 2)], nums[int(l / 2)])

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        nums1, nums2 = (nums1, nums2) if l1 <= l2 else (nums2, nums1)
        l1, l2 = len(nums1), len(nums2)
        if l1 == 0:
            return sum(self.findMedian(nums2)) / 2
        if l1 == 1:
            nums2.append(nums1[0])
            nums2.sort()
            return sum(self.findMedian(nums2)) / 2

        a1, b1 = self.findMedian(nums1)
        a2, b2 = self.findMedian(nums2)
        if a1 <= b2 and a2 <= b1:
            return sum(self.findMedian(sorted([a1, b1, a2, b2]))) / 2
        if a1 > b2:
            return self.findMedianSortedArrays(nums1[:int((l1 + 1) / 2)], nums2[(l1 - int((l1 + 1) / 2)):])
        if b1 < a2:
            return self.findMedianSortedArrays(nums1[int(l1 / 2):], nums2[:-(l1 - int((l1 + 1) / 2))])

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([3], [-2, -1]))
    # nums1 = [1, 2, 3, 4, 5, 6]
    # nums2 = [1, 2, 4, 5, 7, 8]
    # l1 = len(nums1)
    # l2 = len(nums2)
    # print(nums1[int(l1 / 2):])
    # print(nums2[:-(l1 - int((l1 + 1) / 2))])
    # print(nums1[:int((l1 + 1) / 2)])
    # print(nums2[(l1 - int((l1 + 1) / 2)):])
