# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        flags = [True] * len(nums)
        res = []
        maxlen = len(nums)

        def select(n, cur_list):
            if n == maxlen:
                res.append(cur_list[:])
                return
            for i in range(len(flags)):
                if flags[i]:
                    flags[i] = False
                    cur_list.append(nums[i])
                    select(n + 1, cur_list)
                    cur_list.pop()
                    flags[i] = True

        select(0, [])
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    l = [1, 2, 3]
    print(Solution().permute(l))
