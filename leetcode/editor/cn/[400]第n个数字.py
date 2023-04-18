#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] 第N个数字
#
# https://leetcode-cn.com/problems/nth-digit/description/
#
# algorithms
# Easy (33.77%)
# Likes:    75
# Dislikes: 0
# Total Accepted:    5.4K
# Total Submissions: 15.9K
# Testcase Example:  '3'
#
# 在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 个数字。
# 
# 注意:
# n 是正数且在32为整形范围内 ( n < 2^31)。
# 
# 示例 1:
# 
# 
# 输入:
# 3
# 
# 输出:
# 3
# 
# 
# 示例 2:
# 
# 
# 输入:
# 11
# 
# 输出:
# 0
# 
# 说明:
# 第11个数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是0，它是10的一部分。
# 
# 
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        size = 9
        sum = digit * size
        while sum < n:
            digit += 1
            size *= 10
            sum += digit * size
        if sum == n:
            return 9
        pos = n - (sum - digit * size)
        target = int((pos - 1) / digit) + int(size / 9)
        return str(target)[(pos - 1) % digit]

# @lc code=end
if __name__ == "__main__":
    print(Solution().findNthDigit(3))
