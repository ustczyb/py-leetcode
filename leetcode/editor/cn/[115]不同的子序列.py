# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。 
# 
#  字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列
# ，而 "AEC" 不是） 
# 
#  题目数据保证答案符合 32 位带符号整数范围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# rabbbit
# rabbbit
# rabbbit 
# 
#  示例 2： 
# 
#  
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length, t.length <= 1000 
#  s 和 t 由英文字母组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 583 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0] * len(t) for _ in range(len(s))]
        for j in range(len(t)):
            for i in range(j, len(s)):
                if s[i] == t[j]:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = (dp[i - 1][j] if i > 0 else 0) + 1
                else:
                    dp[i][j] = (dp[i - 1][j] if i > 0 else 0)
        return dp[len(s) - 1][len(t) - 1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = "babgbag"
    t = "bag"
    print(Solution().numDistinct(s, t))
