# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。 
# 
#  给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 9 
#  皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。 
#  
#  
#  
#  Related Topics 回溯算法 
#  👍 254 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def totalNQueens(self, n: int) -> int:
        arr = [0] * n
        self.count = 0

        def check(row, position) -> bool:
            # 检查第row行将皇后放入position位置是否会存在冲突
            for i in range(row):
                if position == arr[i]:
                    return False
                if abs(position - arr[i]) == row - i:
                    return False
            return True

        def set(row):
            if row == n:
                self.count += 1
            for i in range(n):
                if check(row, i):
                    arr[row] = i
                    set(row + 1)
                    arr[row] = 0

        set(0)
        return self.count
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().totalNQueens(4))