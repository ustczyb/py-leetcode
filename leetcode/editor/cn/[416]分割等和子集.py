# 给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  注意: 
# 
#  
#  每个数组中的元素不会超过 100 
#  数组的大小不会超过 200 
#  
# 
#  示例 1: 
# 
#  输入: [1, 5, 11, 5]
# 
# 输出: true
# 
# 解释: 数组可以分割成 [1, 5, 5] 和 [11].
#  
# 
#  
# 
#  示例 2: 
# 
#  输入: [1, 2, 3, 5]
# 
# 输出: false
# 
# 解释: 数组不能分割成两个元素和相等的子集.
#  
# 
#  
#  Related Topics 动态规划

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 == 1:
            return False
        target = s / 2
        size = len(nums)
        cache_dict = {}

        def subSulotion(begin_index, target):
            if target == 0:
                return True
            if begin_index == size and target != 0:
                return False
            key = '%d_%d' % (begin_index, target)
            if not key in cache_dict:
                res = subSulotion(begin_index + 1, target - nums[begin_index]) or subSulotion(begin_index + 1, target)
                cache_dict[key] = res
                return res
            else:
                return cache_dict[key]

        return subSulotion(0, target)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().canPartition(
        [1, 5, 11, 5]))
