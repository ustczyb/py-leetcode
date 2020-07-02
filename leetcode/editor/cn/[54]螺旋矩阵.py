# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。 
# 
#  示例 1: 
# 
#  输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2: 
# 
#  输入:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#  
#  Related Topics 数组

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        a1, b1 = 0, 0
        a2, b2 = len(matrix) - 1, len(matrix[0]) - 1
        res = []
        while a1 <= a2 and b1 <= b2:
            res.extend(matrix[a1][b1: b2 + 1])
            a1 += 1
            if a1 > a2:
                break
            for r in range(a1, a2 + 1):
                res.append(matrix[r][b2])
            b2 -= 1
            if b2 < b1:
                break
            if b1 == 0:
                res.extend(matrix[a2][b2::-1])
            else:
                res.extend(matrix[a2][b2:b1 - 1:-1])
            a2 -= 1

            for r in range(a2, a1 - 1, -1):
                res.append(matrix[r][b1])
            b1 += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(Solution().spiralOrder(matrix))
    # print([1, 2, 3, 4][3::-1])
