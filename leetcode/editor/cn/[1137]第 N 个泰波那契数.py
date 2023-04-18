# 泰波那契序列 Tn 定义如下： 
# 
#  T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2 
# 
#  给你整数 n，请返回第 n 个泰波那契数 Tn 的值。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 4
# 输出：4
# 解释：
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#  
# 
#  示例 2： 
# 
#  输入：n = 25
# 输出：1389537
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= n <= 37 
#  答案保证是一个 32 位整数，即 answer <= 2^31 - 1。 
#  
#  Related Topics 记忆化搜索 数学 动态规划 
#  👍 107 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def __init__(self):
        self.res_arr = [-1] * 38
        self.res_arr[0] = 0
        self.res_arr[1] = self.res_arr[2] = 1
        self.cur = 2

    def tribonacci(self, n: int) -> int:
        if n <= self.cur:
            return self.res_arr[n]
        for i in range(self.cur + 1, n + 1):
            self.res_arr[i] = self.res_arr[i - 1] + self.res_arr[i - 2] + self.res_arr[i - 3]
        return self.res_arr[n]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().tribonacci(4))
