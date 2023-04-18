# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。 
# 
#  返回符合要求的 最少分割次数 。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：1
# 解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "ab"
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 2000 
#  s 仅由小写英文字母组成 
#  
#  
#  
#  Related Topics 动态规划 
#  👍 412 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCut(self, s: str) -> int:

        l = len(s)
        if l == 1:
            return 0

        matrix = [[-1] * l for i in range(l)]
        for i in range(l):
            matrix[i][i] = 1

        def cal_value(start_index, end_index):
            if start_index > end_index:
                return -1
            if matrix[start_index][end_index] != -1:
                return matrix[start_index][end_index]
            if s[start_index] == s[end_index]:
                if start_index + 1 == end_index:
                    matrix[start_index][end_index] = 1
                else:
                    matrix[start_index][end_index] = cal_value(start_index + 1, end_index - 1)
            else:
                matrix[start_index][end_index] = 0
            return matrix[start_index][end_index]

        for i in range(l):
            for j in range(i, l):
                cal_value(i, j)

        dp = [-1] * l
        dp[0] = 0
        for i in range(1, l - 1):
            res = l



        # dp = [[-1] * l for i in range(l)]
        # for i in range(l):
        #     for j in range(l):
        #         if matrix[i][j] == 1:
        #             dp[i][j] = 0
        #
        # for step in range(1, l):
        #     for i in range(l - step):
        #         if dp[i][i + step] == -1:
        #             res = step
        #             for j in range(i, i + step):
        #                 if res > dp[i][j] + dp[j + 1][i + step] + 1:
        #                     res = dp[i][j] + dp[j + 1][i + step] + 1
        #             dp[i][i + step] = res
        # return dp[0][l - 1]

        # def cal_len(start_index, end_index) -> int:
        #     if dp[start_index][end_index] != -1:
        #         return dp[start_index][end_index]
        #     res = l
        #     for i in range(start_index, end_index + 1):
        #         if cal_value(start_index, i) == 1:
        #             if i == end_index:
        #                 return 0
        #             sub_res = 1 + cal_len(i + 1, end_index)
        #             if sub_res < res:
        #                 res = sub_res
        #     dp[start_index][end_index] = res
        #     return res

        # if cal_value(0, l - 1) == 1:
        #     return 0
        # return cal_len(0, l - 1)

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print(Solution().minCut(s))