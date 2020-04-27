#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
# https://leetcode-cn.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (50.03%)
# Likes:    72
# Dislikes: 0
# Total Accepted:    10.3K
# Total Submissions: 20.6K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
# 
# 注意:
# 假设字符串的长度不会超过 1010。
# 
# 示例 1: 
# 
# 
# 输入:
# "abccccdd"
# 
# 输出:
# 7
# 
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        for ch in s:
            d[ch] += 1
        res = 0
        flag = False
        for k in d:
            if d[k] % 2 == 0:
                res += d[k]
            else:
                if not flag:
                    flag = True
                    res += d[k]
                else:
                    res += d[k] - 1
        return res
# @lc code=end

