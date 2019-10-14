#
# @lc app=leetcode.cn id=367 lang=python3
#
# [367] 有效的完全平方数
#
# https://leetcode-cn.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (42.08%)
# Likes:    69
# Dislikes: 0
# Total Accepted:    15.4K
# Total Submissions: 36.6K
# Testcase Example:  '16'
#
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
# 
# 说明：不要使用任何内置的库函数，如  sqrt。
# 
# 示例 1：
# 
# 输入：16
# 输出：True
# 
# 示例 2：
# 
# 输入：14
# 输出：False
# 
# 
#

# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 0:
            return False
        a = 1
        b = num / 1
        while abs(a - b) > 1:
            a = int((a + b) / 2)
            b = int(num / a)
        return a * a == num or b * b == num

# @lc code=end

