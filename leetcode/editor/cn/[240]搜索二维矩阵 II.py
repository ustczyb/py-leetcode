# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性： 
# 
#  
#  每行的元素从左到右升序排列。 
#  每列的元素从上到下升序排列。 
#  
# 
#  示例: 
# 
#  现有矩阵 matrix 如下： 
# 
#  [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
#  
# 
#  给定 target = 5，返回 true。 
# 
#  给定 target = 20，返回 false。 
#  Related Topics 二分查找 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row_index = 0
        col_index = len(matrix[0]) - 1
        while row_index < len(matrix) and col_index >= 0:
            if target == matrix[row_index][col_index]:
                return True
            if target < matrix[row_index][col_index]:
                col_index -= 1
            else:
                row_index += 1
        return False
        
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    matrix = [
                [1,   4,  7, 11, 15],
                [2,   5,  8, 12, 19],
                [3,   6,  9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]]
    print(Solution().searchMatrix(matrix, 18))
