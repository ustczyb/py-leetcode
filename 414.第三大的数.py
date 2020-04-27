#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
# https://leetcode-cn.com/problems/third-maximum-number/description/
#
# algorithms
# Easy (32.88%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    12.9K
# Total Submissions: 39.1K
# Testcase Example:  '[3,2,1]'
#
# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。
# 
# 示例 1:
# 
# 
# 输入: [3, 2, 1]
# 
# 输出: 1
# 
# 解释: 第三大的数是 1.
# 
# 
# 示例 2:
# 
# 
# 输入: [1, 2]
# 
# 输出: 2
# 
# 解释: 第三大的数不存在, 所以返回最大的数 2 .
# 
# 
# 示例 3:
# 
# 
# 输入: [2, 2, 3, 1]
# 
# 输出: 1
# 
# 解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
# 存在两个值为2的数，它们都排第二。
# 
# 
#

# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # 因为时间复杂度为O(N), 所以只能一一判断
        r = [float("-inf"), float("-inf"), float("-inf")]
        for n in nums:
            # 重复的值, 无需判断
            if n in r:
                continue
            # 出现最大的值
            if n > r[0]:
                r = [n, r[0], r[1]]
            # 出现第二大的值
            elif n > r[1]:
                r = [r[0], n, r[1]]
            # 出现第三大的值
            elif n > r[2]:
                r[2] = n
    
        return r[0] if math.isinf(r[2]) else r[2]
# @lc code=end

