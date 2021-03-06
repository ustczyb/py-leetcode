#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (46.64%)
# Likes:    69
# Dislikes: 0
# Total Accepted:    13.1K
# Total Submissions: 28.1K
# Testcase Example:  '16'
#
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
# 
# 示例 1:
# 
# 输入: 16
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: 5
# 输出: false
# 
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
# 
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num <= 0:
            return False
        while(num >= 4):
            if num % 4 != 0:
                return False
            num /= 4
        if num != 1:
            return False
        return True
            
# @lc code=end

