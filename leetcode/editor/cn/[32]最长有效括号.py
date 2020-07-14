# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。 
# 
#  示例 1: 
# 
#  输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
#  
# 
#  示例 2: 
# 
#  输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
#  
#  Related Topics 字符串 动态规划


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] != ')':
                continue
            if s[i - 1] == '(':
                if i > 1:
                    dp[i] = dp[i - 2] + 2
                else:
                    dp[i] = 2
            else:
                if i - dp[i - 1] >= 1 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                else:
                    dp[i] = 0
        return max(dp)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().longestValidParentheses(')()())'))
