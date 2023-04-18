# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 100 
#  -104 <= matrix[i][j], target <= 104 
#  
#  Related Topics 数组 二分查找 
#  👍 429 👎 0

from typing import List
# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search row
        low = 0
        high = len(matrix) - 1
        row = -1
        while low < high:
            mid = int((low + high) / 2)
            if matrix[mid + 1][0] <= target:
                if matrix[mid + 1][0] == target:
                    return True
                low = mid + 1
            elif matrix[mid][0] >= target:
                if matrix[mid][0] == target:
                    return True
                high = mid - 1
            else:
                row = mid
                break
        if row == -1:
            row = low

        low = 0
        high = len(matrix[0]) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if matrix[row][mid] < target:
                low = mid + 1
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    matrix = [[1], [3], [5]]
    target = 3
    print(Solution().searchMatrix(matrix, target))
