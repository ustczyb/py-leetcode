# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。 
# 
#  回文串 是正着读和反着读都一样的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：[["a"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 16 
#  s 仅由小写英文字母组成 
#  
#  Related Topics 深度优先搜索 动态规划 回溯算法 
#  👍 657 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        l = len(s)


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

        dp = [[[]] * l for i in range(l)]
        for i in range(l):
            dp[i][i] = [[s[i]]]

        def cal_len(start_index, end_index) -> List[List[str]]:
            if dp[start_index][end_index]:
                return dp[start_index][end_index]
            res = []
            for i in range(start_index, end_index + 1):
                if cal_value(start_index, i) == 1:
                    begin_str = s[start_index: i + 1]
                    if i == end_index:
                        res.append([begin_str])
                    else:
                        for x in cal_len(i + 1, end_index):
                            t = [begin_str] + x
                            res.append(t)
            dp[start_index][end_index] = res
            return res

        return cal_len(0, l - 1)

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = "a"
    print(Solution().partition(s))