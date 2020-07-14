# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def __init__(self):
        self._dict_ = {1: ['()'], 2: ['()()', '(())']}

    def generateParenthesis(self, n: int) -> List[str]:
        if n in self._dict_:
            return self._dict_[n]
        else:
            sub_res = self.generateParenthesis(n - 1)
            res = []
            for s in sub_res:
                res.append('()' + s)
            for i in range(1, n - 1):
                sub_res1 = self.generateParenthesis(i + 1)
                sub_res2 = self.generateParenthesis(n - 1 - i)
                for s1 in sub_res1[-len(self.generateParenthesis(i)):]:
                    for s2 in sub_res2:
                        res.append(s1 + s2)

            for s in sub_res:
                res.append('(' + s + ')')
            self._dict_[n] = res
            return res

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().generateParenthesis(4))
