#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (50.77%)
# Likes:    249
# Dislikes: 0
# Total Accepted:    41.6K
# Total Submissions: 81.9K
# Testcase Example:  '"11"\n"1"'
#
# 给定两个二进制字符串，返回他们的和（用二进制表示）。
# 
# 输入为非空字符串且只包含数字 1 和 0。
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        count_dict = defaultdict(int)
        index = 0
        for i in a[::-1]:
            if i == '1':
                count_dict[index] += 1
            index += 1
        index = 0
        for i in b[::-1]:
            if i == '1':
                count_dict[index] += 1
            index += 1
        for i in range(max(len(a), len(b)) + 1):
            if count_dict[i] >= 2:
                count_dict[i] -= 2
                count_dict[i + 1] += 1
        res = []
        for i in range(max(len(a), len(b)), -1, -1):
            res.append(count_dict[i])
        if res[0] == 0:
            return ''.join(map(str, res[1:]))
        else:
            return ''.join(map(str, res))

# @lc code=end

if __name__ == "__main__":
    print(Solution().addBinary('11', '1'))