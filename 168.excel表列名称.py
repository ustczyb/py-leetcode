#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (34.97%)
# Likes:    137
# Dislikes: 0
# Total Accepted:    13.3K
# Total Submissions: 38K
# Testcase Example:  '1'
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 
# 例如，
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "A"
# 
# 
# 示例 2:
# 
# 输入: 28
# 输出: "AB"
# 
# 
# 示例 3:
# 
# 输入: 701
# 输出: "ZY"
# 
# 
#

# @lc code=start
class Solution:
    def convertToTitle(self, n: int) -> str:
        tmp = []
        while n > 0:
            remain = n % 26
            if remain == 0:
                remain = 26
            tmp.append(remain)
            n = int((n - remain) / 26)
        diff = ord('A') - 1
        res = ''
        for id in reversed(tmp):
            res += str(chr(id + diff))
        return res
# @lc code=end
# if __name__ == "__main__":
#     print(Solution().convertToTitle(27))