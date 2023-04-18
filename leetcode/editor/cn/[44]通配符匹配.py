# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。 
# 
#  '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
#  
# 
#  两个字符串完全匹配才算匹配成功。 
# 
#  说明: 
# 
#  
#  s 可能为空，且只包含从 a-z 的小写字母。 
#  p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。 
#  
# 
#  示例 1: 
# 
#  输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。 
# 
#  示例 2: 
# 
#  输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
#  
# 
#  示例 3: 
# 
#  输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
#  
# 
#  示例 4: 
# 
#  输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
#  
# 
#  示例 5: 
# 
#  输入:
# s = "acdcb"
# p = "a*c?b"
# 输出: false 
#  Related Topics 贪心 递归 字符串 动态规划 
#  👍 738 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s:
            for ch in p:
                if ch != '*':
                    return False
            return True

        if not p:
            return s == p

        dp = [[0] * (len(s)) for _ in range(len(p))]

        count = 0
        for i in range(len(p)):
            if p[i] != '*':
                count += 1
                if count > 1:
                    break
                if p[i] != '?' and p[i] != s[0]:
                    break
                dp[i][0] = 1
            else:
                dp[i][0] = 1

        for p_index in range(len(p)):
            for s_index in range(1, len(s)):
                p_ch = p[p_index]
                s_ch = s[s_index]
                if p_ch == '*':
                    if p_index == 0:
                        dp[p_index][s_index] = 1
                    else:
                        if s_index == 0:
                            dp[p_index][s_index] = dp[p_index - 1][s_index]
                        else:
                            dp[p_index][s_index] = dp[p_index - 1][s_index - 1] or dp[p_index][s_index - 1] or dp[p_index - 1][s_index]
                else:
                    if p_ch == s_ch or p_ch == '?':
                        if p_index == 0:
                            dp[p_index][s_index] = (0 if s_index > 0 else 1)
                        elif s_index == 0:
                            dp[p_index][s_index] = (dp[p_index - 1][s_index] if p[p_index - 1] == '*' else 0)
                        else:
                            dp[p_index][s_index] = dp[p_index - 1][s_index - 1]
                    else:
                        dp[p_index][s_index] = 0
        for row in dp:
            print(row)
        return True if dp[len(p) - 1][len(s) - 1] == 1 else False

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = "ab"
    p = "?*"
    print(Solution().isMatch(s, p))
