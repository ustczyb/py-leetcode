#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#
# https://leetcode-cn.com/problems/is-subsequence/description/
#
# algorithms
# Easy (47.67%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    12.3K
# Total Submissions: 25.7K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 
# 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
# 
# 
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
# 
# 示例 1:
# s = "abc", t = "ahbgdc"
# 
# 返回 true.
# 
# 示例 2:
# s = "axc", t = "ahbgdc"
# 
# 返回 false.
# 
# 后续挑战 :
# 
# 如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T
# 的子序列。在这种情况下，你会怎样改变代码？
# 
# 致谢:
# 
# 特别感谢 @pbrother 添加此问题并且创建所有测试用例。
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 1.预处理 时间复杂度O(len(t))
        ch_dict = defaultdict(list)
        for i in range(len(t)):
            ch_dict[t[i]].append(i)
        # 2.判断是否是子序列
        index_dict = defaultdict(int)
        cur_index = 0
        for ch in s:
            if index_dict[ch] >= len(ch_dict[ch]):
                return False
            while index_dict[ch] < len(ch_dict[ch]) and ch_dict[ch][index_dict[ch]] < cur_index:
                index_dict[ch] += 1
            if index_dict[ch] >= len(ch_dict[ch]):
                return False
            elif ch_dict[ch][index_dict[ch]] == cur_index:
                cur_index += 1
            else:
                cur_index = ch_dict[ch][index_dict[ch]] + 1
        return True
# @lc code=end
if __name__ == "__main__":
    print(Solution().isSubsequence('abc', 'ahbgdc'))
