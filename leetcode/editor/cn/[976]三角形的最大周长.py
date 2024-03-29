# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。 
# 
#  如果不能形成任何面积不为零的三角形，返回 0。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  输入：[2,1,2]
# 输出：5
#  
# 
#  示例 2： 
# 
#  输入：[1,2,1]
# 输出：0
#  
# 
#  示例 3： 
# 
#  输入：[3,2,3,4]
# 输出：10
#  
# 
#  示例 4： 
# 
#  输入：[3,6,2,3]
# 输出：8
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= A.length <= 10000 
#  1 <= A[i] <= 10^6 
#  
#  Related Topics 排序 数学 
#  👍 138 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        for i in range(len(sorted_list) - 1, 1, -1):
            if sorted_list[i] < sorted_list[i - 1] + sorted_list[i - 2]:
                return sum(sorted_list[i - 2: i + 1])
        return 0
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    nums = [3,6,2,3]
    print(Solution().largestPerimeter(nums))