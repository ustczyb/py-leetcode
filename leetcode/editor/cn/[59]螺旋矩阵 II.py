# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。 
# 
#  示例: 
# 
#  输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ] 
#  Related Topics 数组

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 0:
            return []
        if n == 1:
            return [[1]]
        matrix = []
        init_row = [0] * n
        for i in range(n):
            matrix.append(init_row.copy())
        a1, b1 = 0, 0
        a2, b2 = n - 1, n - 1
        cur = 1
        while a1 <= a2 and b1 <= b2:
            for i in range(b1, b2 + 1):
                matrix[a1][i] = cur
                cur += 1
            a1 += 1
            if a1 > a2:
                break

            for r in range(a1, a2 + 1):
                matrix[r][b2] = cur
                cur += 1
            b2 -= 1
            if b2 < b1:
                break

            for i in range(b2, b1 - 1, -1):
                matrix[a2][i] = cur
                cur += 1
            a2 -= 1

            for r in range(a2, a1 - 1, -1):
                matrix[r][b1] = cur
                cur += 1
            b1 += 1
        return matrix


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().generateMatrix(3))
    # print([([0] * 3)])
