# 给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。 
# 
#  示例 1: 
# 
#  输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1。 
# 
#  示例 2: 
# 
#  输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。 
# 
#  说明: 你可以假设 n 不小于 2 且不大于 58。 
#  Related Topics 数学 动态规划 
#  👍 497 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import numpy as np
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2:
            return 1

        def cal_res(split_nums):
            devide_res = int(n / split_nums)
            left = n % split_nums
            return int(np.power(devide_res, (split_nums - left)) * np.power(devide_res + 1, left))

        e = np.exp(1)
        if int(n / e) < 2:
            return cal_res(2)

        split_nums = int(n / e)
        res1 = cal_res(split_nums)
        split_nums = int(n / e) - 1
        res2 = cal_res(split_nums)
        split_nums = int(n / e) + 1
        res3 = cal_res(split_nums)
        return int(max(res1, res2, res3))

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().integerBreak(30))