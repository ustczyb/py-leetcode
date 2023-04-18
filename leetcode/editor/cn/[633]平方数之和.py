# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a2 + b2 = c 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
#  
# 
#  示例 2： 
# 
#  输入：c = 3
# 输出：false
#  
# 
#  示例 3： 
# 
#  输入：c = 4
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：c = 2
# 输出：true
#  
# 
#  示例 5： 
# 
#  输入：c = 1
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= c <= 231 - 1 
#  
#  Related Topics 数学 双指针 二分查找 
#  👍 294 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(math.sqrt(c))
        left = 0
        right = n
        while (left <= right):
            res = left * left + right * right - c
            if res == 0:
                return True
            elif res > 0:
                right -= 1
            else:
                left += 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
