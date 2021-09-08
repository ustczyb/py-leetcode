# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。 
# 
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。 
# 
#  示例 2： 
# 
#  
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 
# 。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= k <= 100 
#  0 <= prices.length <= 1000 
#  0 <= prices[i] <= 1000 
#  
#  Related Topics 数组 动态规划 
#  👍 569 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        dp = [[0] * len(prices) for _ in range(2 * k + 1)]
        for i in range(1, 2 * k + 1):
            for j in range(i - 1, len(prices)):
                if i % 2 == 1:
                    dp[i][j] = max((dp[i - 1][j - 1] if j > 0 else 0) - prices[j],
                                   dp[i][j - 1] if j > i - 1 else -prices[i - 1])
                else:
                    dp[i][j] = max((dp[i - 1][j - 1] if j > 0 else 0) + prices[j], dp[i][j - 1] if j > 0 else 0)
        res = 0
        for i in range(len(dp)):
            if res < dp[i][len(prices) - 1]:
                res = dp[i][len(prices) - 1]
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    k = 2
    prices = [1, 2, 4, 7]
    print(Solution().maxProfit(k, prices))
