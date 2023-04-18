#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#
# https://leetcode-cn.com/problems/ransom-note/description/
#
# algorithms
# Easy (50.11%)
# Likes:    57
# Dislikes: 0
# Total Accepted:    11K
# Total Submissions: 21.9K
# Testcase Example:  '"a"\n"b"'
#
# 给定一个赎金信 (ransom)
# 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true
# ；否则返回 false。
# 
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)
# 
# 注意：
# 
# 你可以假设两个字符串均只含有小写字母。
# 
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_dict = defaultdict(int)
        magazine_dict = defaultdict(int)
        for ch in ransomNote:
            ransom_dict[ch] += 1
        for ch in magazine:
            magazine_dict[ch] += 1
        for k in ransom_dict:
            if magazine_dict[k] < ransom_dict[k]:
                return False
        return True

# @lc code=end

