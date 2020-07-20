# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。 
# 
#  示例 1 : 
# 
#  
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
#  
# 
#  说明 : 
# 
#  
#  数组的长度为 [1, 20,000]。 
#  数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。 
#  
#  Related Topics 数组 哈希表

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
from  collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_arr = [0]
        sum_dict = defaultdict(list)
        res = 0
        for i in range(1, len(nums) + 1):
            sum_arr.append(sum_arr[i - 1] + nums[i - 1])
        for i in range(len(sum_arr)):
            sum_dict[sum_arr[i]].append(i)
        for i in range(len(sum_arr)):
            if sum_arr[i] + k in sum_dict:
                index_list = sum_dict[sum_arr[i] + k]
                for j in index_list:
                    if j > i:
                        res += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().subarraySum([1, 1, 1], k=2))
