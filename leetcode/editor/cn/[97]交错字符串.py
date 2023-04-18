# 给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。 
# 
#  两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串： 
# 
#  
#  s = s1 + s2 + ... + sn 
#  t = t1 + t2 + ... + tm 
#  |n - m| <= 1 
#  交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ... 
#  
# 
#  提示：a + b 意味着字符串 a 和 b 连接。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：s1 = "", s2 = "", s3 = ""
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s1.length, s2.length <= 100 
#  0 <= s3.length <= 200 
#  s1、s2、和 s3 都由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 432 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        l1, l2, l3 = len(s1), len(s2), len(s3)
        if l1 + l2 != l3:
            return False

        dp = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        def isAppend(index1, index2):
            if dp[index1][index2] != -1:
                return dp[index1][index2]
            if index1 == l1:
                dp[index1][index2] = (s2[index2:] == s3[index1 + index2:])
                return dp[index1][index2]
            if index2 == l2:
                dp[index1][index2] = (s1[index1:] == s3[index1 + index2:])
                return dp[index1][index2]
            if s1[index1] == s3[index1 + index2]:
                if isAppend(index1 + 1, index2):
                    dp[index1][index2] = True
                    return True
            if s2[index2] == s3[index1 + index2]:
                if isAppend(index1, index2 + 1):
                    dp[index1][index2] = True
                    return True
            dp[index1][index2] = False
            return False

        return isAppend(0, 0)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"

    print(Solution().isInterleave(s1, s2, s3))
