# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。 
# 
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入：prices = [3,3,5,0,0,3,1,4]
# 输出：6
# 解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
#      随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。 
# 
#  示例 2： 
# 
#  
# 输入：prices = [1,2,3,4,5]
# 输出：4
# 解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
#      因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#  
# 
#  示例 3： 
# 
#  
# 输入：prices = [7,6,4,3,1] 
# 输出：0 
# 解释：在这个情况下, 没有交易完成, 所以最大利润为 0。 
# 
#  示例 4： 
# 
#  
# 输入：prices = [1]
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 105 
#  0 <= prices[i] <= 105 
#  
#  Related Topics 数组 动态规划 
#  👍 826 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
# 下面为原创解法 空间复杂度较最优解更高 建议学习最优的动态规划解法
    def max_profit(self, prices: List[int]) -> (int, int, int):
        res = 0
        start_index = 0
        res_start_index = 0
        res_end_index = 0
        dp = 0
        for i in range(1, len(prices)):
            dp += prices[i] - prices[i - 1]
            if dp < 0:
                dp = 0
                start_index = i
            if dp > res:
                res = dp
                res_end_index = i
                res_start_index = start_index
        return res, res_start_index, res_end_index

    def max_two_profit(self, prices: List[int]) -> int:
        res = prices[-1] - prices[0]
        if len(prices) < 4:
            return res
        max_from_left = [prices[1]] * (len(prices) - 2)
        min_from_right = [prices[-2]] * (len(prices) - 2)
        for i in range(1, len(prices) - 2):
            max_from_left[i] = max(prices[i + 1], max_from_left[i - 1])
            min_from_right[-1 - i] = min(min_from_right[-i], prices[len(prices) - 2 - i])
        return res + max([max_from_left[i] - min_from_right[i + 1] for i in range(len(prices) - 3)])

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        max_profit, start_index, end_index = self.max_profit(prices)
        res1 = max_profit + max(self.max_profit(prices[:start_index])[0], self.max_profit(prices[end_index + 1:])[0])
        res2 = self.max_two_profit(prices[start_index:end_index + 1])
        return max(res1, res2)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    prices = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0, 9]
    print(Solution().maxProfit(prices))
