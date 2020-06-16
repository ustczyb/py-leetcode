# 给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的每个数字在每个组合中只能使用一次。 
# 
#  说明： 
# 
#  
#  所有数字（包括目标数）都是正整数。 
#  解集不能包含重复的组合。 
#  
# 
#  示例 1: 
# 
#  输入: candidates = [10,1,2,7,6,1,5], target = 8,
# 所求解集为:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#  
# 
#  示例 2: 
# 
#  输入: candidates = [2,5,2,1,2], target = 5,
# 所求解集为:
# [
#   [1,2,2],
#   [5]
# ] 
#  Related Topics 数组 回溯算法

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.combinationSortedSum(candidates, target)

    def combinationSortedSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 1 or target < nums[0]:
            return []
        res = []
        i = 0
        while i < len(nums):
            num = nums[i]
            if num == target:
                res.append([num])
                # i移动到下一个不重复的数
                while i < len(nums) and nums[i] == num:
                    i += 1
            elif num > target:
                break
            else:
                tmp = self.combinationSortedSum(nums[i + 1:], target - num)
                if tmp:
                    for sub_list in tmp:
                        res.append([num] + sub_list)
                while i < len(nums) and nums[i] == num:
                    i += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
