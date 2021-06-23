# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。 
# 
#  示例: 
# 
#  输入: n = 4, k = 2
# 输出:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ] 
#  Related Topics 回溯算法 
#  👍 569 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        def choose(start, k) -> List[List[int]]:
            # 返回[start, n]中选择k个数的所有组合
            if k <= 0:
                return [[]]
            if n - start + 1 < k:
                return [[]]
            if n - start + 1 == k:
                return [list(range(start, n + 1))]
            res = []
            for i in range(start, n - k + 2):
                sub_res = choose(i + 1, k - 1)
                res.extend([[i] + l for l in sub_res])
            return res

        return choose(1, k)

# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().combine(4, 2))