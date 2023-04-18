#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#
# https://leetcode-cn.com/problems/find-the-difference/description/
#
# algorithms
# Easy (58.55%)
# Likes:    91
# Dislikes: 0
# Total Accepted:    14.8K
# Total Submissions: 25.3K
# Testcase Example:  '"abcd"\n"abcde"'
#
# 给定两个字符串 s 和 t，它们只包含小写字母。
# 
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
# 
# 请找出在 t 中被添加的字母。
# 
# 
# 
# 示例:
# 
# 输入：
# s = "abcd"
# t = "abcde"
# 
# 输出：
# e
# 
# 解释：
# 'e' 是那个被添加的字母。
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for ch in s:
            s_dict[ch] += 1
        for ch in t:
            t_dict[ch] += 1
        for k in t_dict:
            if t_dict[k] == s_dict[k] + 1:
                return k
# @lc code=end

