#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
# https://leetcode-cn.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (31.17%)
# Likes:    136
# Dislikes: 0
# Total Accepted:    44.9K
# Total Submissions: 144.1K
# Testcase Example:  '"Hello World"'
#
# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
# 
# 如果不存在最后一个单词，请返回 0 。
# 
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
# 
# 示例:
# 
# 输入: "Hello World"
# 输出: 5
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 1:
            if s[0] == ' ':
                return 0
            return 1
        res = 0
        l = len(s)
        for i in range(l):
            if s[l - i - 1] != ' ':
                res += 1
            if s[l - i - 1] == ' ' and res > 0:
                return res
        return res
# @lc code=end

if __name__ == "__main__":
    print(Solution().lengthOfLastWord('hello world'))