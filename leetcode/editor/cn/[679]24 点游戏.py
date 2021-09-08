# 你有 4 张写有 1 到 9 数字的牌。你需要判断是否能通过 *，/，+，-，(，) 的运算得到 24。 
# 
#  示例 1: 
# 
#  输入: [4, 1, 8, 7]
# 输出: True
# 解释: (8-4) * (7-1) = 24
#  
# 
#  示例 2: 
# 
#  输入: [1, 2, 1, 2]
# 输出: False
#  
# 
#  注意: 
# 
#  
#  除法运算符 / 表示实数除法，而不是整数除法。例如 4 / (1 - 2/3) = 12 。 
#  每个运算符对两个数进行运算。特别是我们不能用 - 作为一元运算符。例如，[1, 1, 1, 1] 作为输入时，表达式 -1 - 1 - 1 - 1 是不允
# 许的。 
#  你不能将数字连接在一起。例如，输入为 [1, 2, 1, 2] 时，不能写成 12 + 12 。 
#  
#  Related Topics 数组 数学 回溯 
#  👍 320 👎 0

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def judgePoint24(self, cards: List) -> bool:
        if len(cards) == 1 and 1e-6 > abs(cards[0] - 24):
            return True
        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                if self.judgePoint24([cards[i] + cards[j]] + cards[:i] + cards[i + 1: j] + cards[j + 1:]):
                    return True
                if self.judgePoint24([cards[i] - cards[j]] + cards[:i] + cards[i + 1: j] + cards[j + 1:]):
                    return True
                if self.judgePoint24([cards[j] - cards[i]] + cards[:i] + cards[i + 1: j] + cards[j + 1:]):
                    return True
                if self.judgePoint24([cards[i] * cards[j]] + cards[:i] + cards[i + 1: j] + cards[j + 1:]):
                    return True
                if cards[j] > 0 and self.judgePoint24(
                        [cards[i] / cards[j]] + cards[:i] + cards[i + 1: j] + cards[j + 1:]):
                    return True
                if cards[i] > 0 and self.judgePoint24(
                        [cards[j] / cards[i]] + cards[:i] + cards[i + 1: j] + cards[j + 1:]):
                    return True
        return False


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    cards = [3, 8, 3, 8]
    print(Solution().judgePoint24(cards))
