# 给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,2]
# 输出：
# [[1,1,2],
#  [1,2,1],
#  [2,1,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 8 
#  -10 <= nums[i] <= 10 
#  
#  Related Topics 回溯算法 
#  👍 731 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        # 统计字符个数
        num_counter = defaultdict(int)
        for num in nums:
            num_counter[num] += 1

        res = []
        cur_list = []

        def select(n):
            if n > len(nums):
                res.append(cur_list[:])
                return
            for num in num_counter:
                if num_counter[num] > 0:
                    cur_list.append(num)
                    num_counter[num] -= 1
                    select(n + 1)
                    cur_list.pop()
                    num_counter[num] += 1

        select(1)
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().permuteUnique(nums))