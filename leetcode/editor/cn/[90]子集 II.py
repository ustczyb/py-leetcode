# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
#  
#  
#  Related Topics 数组 回溯算法 
#  👍 567 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sub_dict = {}
        for num in nums:
            if num not in sub_dict:
                sub_dict[num] = [[], [num]]
            else:
                sub_dict[num].append([num] * (len(sub_dict[num])))
        
        last_subset = [[]]
        for num in sub_dict:
            res = []
            for l in last_subset:
                for c in sub_dict[num]:
                    res.append(l + c)
            last_subset = res
        return last_subset
        
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().subsetsWithDup([1,2,2]))