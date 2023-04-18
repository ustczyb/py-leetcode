#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        for i in range(int(len(num_str) / 2)):
            if num_str[i] != num_str[-(i + 1)]:
                return False
        return True
        
# @lc code=end

# if __name__ == "__main__":
#     print(Solution().isPalindrome(121))