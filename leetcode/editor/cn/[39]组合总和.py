# 给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。 
# 
#  candidates 中的数字可以无限制重复被选取。 
# 
#  说明： 
# 
#  
#  所有数字（包括 target）都是正整数。 
#  解集不能包含重复的组合。 
#  
# 
#  示例 1: 
# 
#  输入: candidates = [2,3,6,7], target = 7,
# 所求解集为:
# [
#   [7],
#   [2,2,3]
# ]
#  
# 
#  示例 2: 
# 
#  输入: candidates = [2,3,5], target = 8,
# 所求解集为:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ] 
#  Related Topics 数组 回溯算法

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.combinationSortedSum(candidates, target)

    def combinationSortedSum(self, nums: List[int], target: int) -> List[List[int]]:
        if target < nums[0]:
            return []
        res = []
        for i in range(len(nums)):
            num = nums[i]
            if num == target:
                res.append([num])
            elif num > target:
                break
            else:
                tmp = self.combinationSortedSum(nums[i:], target - num)
                if tmp:
                    for sub_list in tmp:
                        res.append([num] + sub_list)
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
