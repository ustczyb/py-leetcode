# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。 
# 
#  说明：解集不能包含重复的子集。 
# 
#  示例: 
# 
#  输入: nums = [1,2,3]
# 输出:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ] 
#  Related Topics 位运算 数组 回溯算法

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def select(n, begin_index, end_len, cur_list):
            if maxlen - begin_index < end_len - n:
                return
            if n == end_len:
                res.append(cur_list[:])
                return
            for i in range(begin_index, len(flags)):
                if flags[i]:
                    flags[i] = False
                    cur_list.append(nums[i])
                    select(n + 1, i + 1, end_len, cur_list)
                    cur_list.pop()
                    flags[i] = True

        maxlen = len(nums)
        flags = [True] * maxlen
        res = [nums]
        for i in range(maxlen):
            select(0, 0, i, [])
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
