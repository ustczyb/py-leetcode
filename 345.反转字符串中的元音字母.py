#
# @lc app=leetcode.cn id=345 lang=python3
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (48.02%)
# Likes:    61
# Dislikes: 0
# Total Accepted:    15.9K
# Total Submissions: 33.1K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 
# 示例 1:
# 
# 输入: "hello"
# 输出: "holle"
# 
# 
# 示例 2:
# 
# 输入: "leetcode"
# 输出: "leotcede"
# 
# 说明:
# 元音字母不包含字母"y"。
# 
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_set = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        vowel_index = []
        for i in range(len(s)):
            ch = s[i]
            if ch in vowel_set:
                vowel_index.append(i)
        l = len(vowel_index)
        t = list(s)
        for i in range(int(l / 2)):
            t[vowel_index[i]], t[vowel_index[l - 1 - i]] = t[vowel_index[l - 1 - i]], t[vowel_index[i]]
        return ''.join(t)
# @lc code=end

